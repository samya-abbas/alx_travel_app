# 🌍 ALX Travel App

Welcome to **alx_travel_app**, a real-world Django-based travel listing and booking platform. This project is part of the ALX Software Engineering curriculum, designed to teach scalable backend design, API documentation, and database integration using industry best practices.

---

## 🚀 Features

- 🔐 Secure Django project with modular settings
- 🧳 Room listing and booking system
- 📅 Booking calendar and availability management
- 📦 MySQL database integration
- 📄 Auto-generated API docs with Swagger (drf-yasg)
- 🔁 CORS and REST API-ready
- 🛠️ Production-ready configuration using environment variables

---

## 🏗️ Project Structure

```
alx_travel_app/
├── alx_travel_app/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── listings/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── .env
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/alx_travel_app.git
cd alx_travel_app
```

### 2. Create Virtual Environment & Activate

```bash
python -m venv venv
source venv/bin/activate  # For Unix/Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file at the project root:

```env
DEBUG=True
SECRET_KEY=your_secret_key_here
DB_NAME=alx_db
DB_USER=root
DB_PASSWORD=your_db_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 5. Setup the Database

```bash
python manage.py migrate
```

### 6. Run the Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📚 API Documentation

Swagger UI is available at:

> [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

Use this interface to test endpoints, view schemas, and interact with your API.

---

## ✨ Tech Stack

- **Python 3.10+**
- **Django**
- **Django REST Framework**
- **MySQL**
- **drf-yasg** – Swagger/OpenAPI docs
- **django-environ** – Environment config
- **django-cors-headers**

---

## 📁 Example API Endpoints

| Method | Endpoint                  | Description                |
|--------|---------------------------|----------------------------|
| GET    | `/api/listings/`          | List all listings          |
| POST   | `/api/listings/`          | Create a new listing       |
| GET    | `/api/listings/<uuid>/`   | Retrieve a specific listing|
| PUT    | `/api/listings/<uuid>/`   | Update a listing           |
| DELETE | `/api/listings/<uuid>/`   | Delete a listing           |

---

## 🧪 Testing

You can use Swagger UI or tools like Postman to test the endpoints. Authentication and rate-limiting can be added in future iterations.

---

## 🧑‍💻 Author

**Samya Abbas**  
ALX SE Student  
[GitHub](https://github.com/samya-abbas)

---

## 📄 License

This project is licensed under the MIT License.

---

> 💡 *This is just the beginning. Future milestones will include Celery tasks, user auth, payment integration, and deployment to production!*