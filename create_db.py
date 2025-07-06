import sqlite3

# Conectarse o crear la base de datos george.db
conn = sqlite3.connect('george.db')

# Crear cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear tabla "estadisticas"
cursor.execute("""
CREATE TABLE IF NOT EXISTS estadisticas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    carreras INTEGER,
    victorias INTEGER,
    podios INTEGER,
    puntos INTEGER
)
""")

# Insertar una fila con estadísticas reales
cursor.execute("""
INSERT INTO estadisticas (carreras, victorias, podios, puntos)
VALUES (104, 1, 11, 468)
""")

# Guardar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Base de datos creada y estadísticas insertadas correctamente.")
