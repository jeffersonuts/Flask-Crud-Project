from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'clave_supersecreta'  # Necesaria para usar flash y usar sesiones

# Página principal
@app.route("/")
def home():
    conn = sqlite3.connect("george.db")
    cursor = conn.cursor()
    cursor.execute("SELECT carreras, victorias, podios, puntos FROM estadisticas ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        carreras, victorias, podios, puntos = resultado
    else:
        carreras = victorias = podios = puntos = 0  # Valores por defecto si no hay datos

    return render_template("index.html",
                           carreras=carreras,
                           victorias=victorias,
                           podios=podios,
                           puntos=puntos)

# Login de administrador
@app.route("/admin_login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        clave = request.form.get("clave")
        if clave == "admin123":
            session["admin_autenticado"] = True
            return redirect(url_for("admin"))
        else:
            flash("Clave incorrecta")
            return redirect(url_for("admin_login"))
    return render_template("admin_login.html")

# Panel de administración con CRUD integrado
@app.route("/admin")
def admin():
    if not session.get("admin_autenticado"):
        return redirect(url_for("admin_login"))

    conn = sqlite3.connect("george.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM estadisticas ORDER BY id DESC LIMIT 1")
    estadisticas = cursor.fetchone()

    cursor.execute("SELECT * FROM estadisticas ORDER BY id DESC")
    registros = cursor.fetchall()

    conn.close()
    return render_template("admin.html", estadisticas=estadisticas, registros=registros)

# Actualizar estadística principal
@app.route("/actualizar_estadisticas", methods=["POST"])
def actualizar_estadisticas():
    carreras = request.form.get("carreras")
    victorias = request.form.get("victorias")
    podios = request.form.get("podios")
    puntos = request.form.get("puntos")

    conn = sqlite3.connect("george.db")
    cursor = conn.cursor()

    cursor.execute("SELECT id FROM estadisticas ORDER BY id DESC LIMIT 1")
    resultado = cursor.fetchone()

    if resultado:
        estadistica_id = resultado[0]
        cursor.execute("""
            UPDATE estadisticas SET carreras = ?, victorias = ?, podios = ?, puntos = ?
            WHERE id = ?
        """, (carreras, victorias, podios, puntos, estadistica_id))
        conn.commit()
        flash("Estadísticas actualizadas correctamente.")
    else:
        flash("No hay estadísticas para actualizar.")

    conn.close()
    return redirect(url_for("admin"))

# Crear nueva estadística
@app.route("/crear_estadistica", methods=["GET", "POST"])
def crear_estadistica():
    if request.method == "POST":
        carreras = request.form.get("carreras")
        victorias = request.form.get("victorias")
        podios = request.form.get("podios")
        puntos = request.form.get("puntos")

        conn = sqlite3.connect("george.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO estadisticas (carreras, victorias, podios, puntos) VALUES (?, ?, ?, ?)",
                       (carreras, victorias, podios, puntos))
        conn.commit()
        conn.close()

        flash("Nueva estadística creada correctamente.")
        return redirect(url_for("admin"))
    return redirect(url_for("admin"))

# Editar estadística desde tabla
@app.route("/editar_estadistica/<int:id>", methods=["GET", "POST"])
def editar_estadistica(id):
    if request.method == "POST":
        carreras = request.form.get("carreras")
        victorias = request.form.get("victorias")
        podios = request.form.get("podios")
        puntos = request.form.get("puntos")

        conn = sqlite3.connect("george.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE estadisticas SET carreras = ?, victorias = ?, podios = ?, puntos = ?
            WHERE id = ?
        """, (carreras, victorias, podios, puntos, id))
        conn.commit()
        conn.close()

        flash(f"Estadística con ID {id} editada correctamente.")
        return redirect(url_for("admin"))
    return redirect(url_for("admin"))

# Eliminar estadística
@app.route("/eliminar_estadistica/<int:id>")
def eliminar_estadistica(id):
    conn = sqlite3.connect("george.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM estadisticas WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    flash(f"Estadística con ID {id} eliminada.")
    return redirect(url_for("admin"))

# Logout
@app.route("/logout")
def logout():
    session.pop("admin_autenticado", None)
    flash("Sesión cerrada.")
    return redirect(url_for("home"))

# Galería
@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

# Contacto
@app.route("/contacto")
def contacto():
    return render_template("contacto.html")

# Procesar formulario de suscripción
@app.route("/procesar_suscripcion", methods=["POST"])
def procesar_suscripcion():
    nombre = request.form.get("nombre")
    correo = request.form.get("email")
    acepta = request.form.get("acepta")  # checkbox devuelve "on" si está marcado

    if not nombre or not correo or acepta != "on":
        flash("Por favor completa todos los campos y acepta los términos.")
        return redirect(url_for("contacto"))

    print(f"Nuevo suscriptor: {nombre} - {correo}")
    flash("¡Gracias por suscribirte a nuestras novedades!")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
