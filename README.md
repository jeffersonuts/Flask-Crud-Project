📄 [English version here](README_EN.md)

# George Russell Web App 🏎️

Este es un proyecto desarrollado con **Flask** que presenta una página web dedicada al piloto de Fórmula 1 **George Russell**.  
La aplicación permite mostrar información, estadísticas, imágenes, y cuenta con un panel de administrador protegido mediante autenticación para realizar operaciones **CRUD** sobre la base de datos.

---

## 🧩 Características principales

- Página principal con información general sobre George Russell.
- Galería de imágenes con lightbox.
- Página de contacto con formulario de suscripción.
- Panel de administrador con login para:
  - Crear nuevas entradas (Create).
  - Ver estadísticas (Read).
  - Actualizar estadísticas (Update).
  - Eliminar entradas (Delete).
- Estilos personalizados con CSS.
- Base de datos **SQLite** (`george.db`) para almacenar las estadísticas.
- Organización modular con carpetas para CSS, JS, imágenes y plantillas.

---

## 🗂️ Estructura del proyecto

```
/project-root
│
├── app.py
├── george.db
├── /static
│   ├── /css
│   │   ├── base.css
│   │   ├── contacto.css
│   │   └── admin.css
│   ├── /js
│   └── /images
│       └── galeria/
├── /templates
│   ├── index.html
│   ├── galeria.html
│   ├── contacto.html
│   ├── login.html
│   └── admin.html
└── README.md
```

---

## ⚙️ Instalación y ejecución

### 1. Clonar el repositorio

```bash
git clone https://github.com/jeffersonuts/Flask-Crud-Project.git
cd george-russell-flask
```

### 2. Crear y activar entorno virtual (opcional pero recomendado)

```bash
# En sistemas Unix/macOS:
python3 -m venv venv
source venv/bin/activate

# En Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install flask
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

Abrir en el navegador:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔐 Acceso al panel de administrador

- **Usuario:** `admin`  
- **Contraseña por defecto:** `admin`  
  ⚠️ *Se recomienda modificarla en `app.py` o implementar un sistema de autenticación con hash para mayor seguridad.*

---

## 🚧 Funcionalidades pendientes / mejoras futuras

- Implementar hash de contraseñas.
- Validaciones más robustas en formularios.
- Sección de noticias o actualizaciones.
- Versión en inglés.

---

## 👨‍💻 Créditos

Proyecto desarrollado por **Jefferson Nuñez Romero** como ejercicio de aprendizaje con Flask y desarrollo web.

---
