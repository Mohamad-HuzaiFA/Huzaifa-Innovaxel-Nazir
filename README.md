# Huzaifa-Innovaxel-Nazir

# 🔗 URL Shortener API — Innovaxel Assessment

This is a take-home assignment for Innovaxel — a simple URL shortener API built with **Django**, **Django REST Framework**, and **MySQL**. It allows users to shorten long URLs, retrieve original ones using short codes, track access count, and manage them via CRUD operations.

---

## ⚙️ Tech Stack

- Python 3.12
- Django 5.x
- Django REST Framework
- MySQL (with `pymysql` connector)
- Pipenv (virtual environment & dependency management)

---

## 🛠️ Local Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/<your-username>/huzaifa-innovaxel-nazeer.git
cd huzaifa-innovaxel-nazeer
git checkout dev
```

### 2️⃣ Setup Virtual Environment

```bash
pip install pipenv
pipenv install
pipenv shell
```

### 3️⃣ Configure MySQL Database

Login to MySQL:

```bash
CREATE DATABASE urlshortener CHARACTER SET utf8mb4;
CREATE USER 'django_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'yourpassword';
GRANT ALL PRIVILEGES ON urlshortener.\* TO 'django_user'@'localhost';
FLUSH PRIVILEGES;
```

Then update DATABASES in config/settings.py:

```bash

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'urlshortener',
        'USER': 'django_user',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Also at the top of settings.py:

```bash
import pymysql
pymysql.install_as_MySQLdb()
```

### 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Run the Server

```bash
python manage.py runserver
```

Test via Postman or browser:

```bash
http://127.0.0.1:8000/
```

# API Endpoints

```bash
Method Endpoint Description
POST /shorten Create a new short URL
GET /shorten/<shortCode> Retrieve and redirect to original URL
PUT /shorten/<shortCode>/update Update the long/original URL
DELETE /shorten/<shortCode>/delete Delete the short URL
GET /shorten/<shortCode>/stats View access count
GET /shorten/all/ View all shortened URLs
```

# 📌 Notes

```bash
URL validation is enforced using DRF serializers.

Short codes are unique and randomly generated.

Access count increases on every GET call.

MySQL is used to simulate a real-world environment.

Minimum 15 commits will be added for review.
```

# 📧 Contact

```bash
For any follow-up, feel free to reach out.

Developer: Huzaifa Nazeer

Email: [huzaifa010.muhammad@gmail.com]
```
