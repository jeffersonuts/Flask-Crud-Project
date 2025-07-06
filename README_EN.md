# George Russell Web App 🏎️

This is a project developed using **Flask**, featuring a website dedicated to Formula 1 driver **George Russell**.  
The application displays information, statistics, and images, and includes an admin panel protected by authentication to perform **CRUD** operations on the database.

---

## 🧩 Main Features

- Homepage with general information about George Russell.
- Image gallery with lightbox.
- Contact page with subscription form.
- Admin panel with login for:
  - Creating new entries (Create).
  - Viewing statistics (Read).
  - Updating statistics (Update).
  - Deleting entries (Delete).
- Custom styles with CSS.
- **SQLite** database (`george.db`) to store statistics.
- Modular folder organization for CSS, JS, images, and templates.

---

## 🗂️ Project Structure

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

## ⚙️ Installation and Execution

### 1. Clone the repository

```bash
git clone https://github.com/jeffersonuts/Flask-Crud-Project.git
cd george-russell-flask
```

### 2. Create and activate a virtual environment (optional but recommended)

```bash
# On Unix/macOS:
python3 -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

Open in your browser:  
[http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## 🔐 Admin Panel Access

- **Username:** `admin`  
- **Default password:** `admin`  
  ⚠️ *It is recommended to change this in `app.py` or implement a hashed authentication system for improved security.*

---

## 🚧 Pending Features / Future Improvements

- Implement password hashing.
- Stronger form validations.
- News or updates section.
- English version of the website.

---

## 👨‍💻 Credits

Project developed by **Jefferson Nuñez Romero** as a learning exercise using Flask and web development.

---
