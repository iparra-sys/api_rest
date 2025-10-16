# API REST con Flask y MySQL

Este proyecto es una API REST básica desarrollada con **Flask**, **Flask-RESTful** y **MySQL**. Permite crear, leer, actualizar y eliminar ítems (`CRUD`) en una base de datos.

---

## 🔹 Características

- Listar todos los ítems (`GET /items`)
- Obtener un ítem por ID (`GET /items/<id>`)
- Crear un nuevo ítem (`POST /items`)
- Actualizar un ítem existente (`PUT /items/<id>`)
- Eliminar un ítem (`DELETE /items/<id>`)
- Base de datos MySQL con SQLAlchemy

---

## 📂 Estructura del proyecto

```
api_rest/
│
├── app.py # Archivo principal del servidor Flask
├── config.py # Configuración de la base de datos MySQL
├── models.py # Modelos de SQLAlchemy
├── requirements.txt # Dependencias del proyecto
├── resources/
│ └── item_resource.py # Endpoints REST
└── README.md
```

---

## ⚙️ Instalación

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
cd api_rest
```

2. Crear y activar un entorno virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3.Instalar dependencias:
```bash
pip install -r requirements.txt
```
4.Configurar la base de datos MySQL en config.py:
```
MYSQL_HOST = "localhost"
MYSQL_USER = "iveth_user"
MYSQL_PASSWORD = "Angel1308."
MYSQL_DB = "api_rest_db"
```
5.Ejecutar la API:
```bash
python app.py
```

El servidor estará corriendo en: http://127.0.0.1:5000

🧩 Endpoints

GET todos los ítems
```bash
GET /items
```

GET un ítem por ID
```bash
GET /items/<id>
```

POST crear un nuevo ítem
Body JSON:
```bash
{
    "name": "Lapicero",
    "description": "Color azul"
}
```

PUT actualizar un ítem
```bash
PUT /items/<id>
```
Body JSON:
```bash
{
    "name": "Cuaderno",
    "description": "Tamaño A4"
}
```

DELETE eliminar un ítem
```bash
DELETE /items/<id>
```

✅ Notas

Asegúrate de que MySQL esté corriendo y que la base de datos api_rest_db exista.
SQLAlchemy crea automáticamente la tabla items la primera vez que ejecutas app.py.
Puedes probar la API con Postman, PowerShell (Invoke-RestMethod) o navegador (solo GET).

📌 Autor

Iveth Parra Herrera