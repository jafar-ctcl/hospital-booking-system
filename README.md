# Clinic Care Hospital - Hospital Booking System

A robust and responsive web application built with **Django** and **Bootstrap 5** for managing hospital operations and patient appointments. This system allows users to view doctor profiles, browse departments, and book appointments seamlessly.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Django Version](https://img.shields.io/badge/django-5.0%2B-green.svg)

## 🚀 Features

-   **User-Friendly Interface**: Modern, responsive design using Bootstrap 5.
-   **Home Page**: Dynamic hero carousel, service highlights, and quick stats.
-   **Doctor Management**: Comprehensive list of doctors with their specializations and department details.
-   **Department Showcase**: Detailed views of hospital departments.
-   **Appointment Booking**: Easy-to-use form for patients to book appointments.
-   **Confirmation System**: Instant visual confirmation upon successful booking.
-   **Contact & About**: Informational pages for hospital details and contact queries.
-   **Admin Dashboard**: Full control for administrators to manage doctors, departments, and bookings via the Django Admin panel.

## 🛠️ Technology Stack

-   **Backend**: Python, Django
-   **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
-   **Database**: SQLite (Default) / PostgreSQL (Ready)
-   **Styling**: Custom CSS with glassmorphism and modern UI effects

## ⚙️ Installation & Setup

Follow these steps to set up the project locally.

### Prerequisites

-   Python 3.8 or higher installed.
-   Git installed.

### 1. Clone the Repository

```bash
git clone https://github.com/jafar-ctcl/hospital-booking-system.git
cd hospital-booking-system
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

Set up the database tables.

```bash
python manage.py migrate
```

### 5. Create a Superuser (Optional)

To access the admin panel.

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

Open your browser and navigate to `http://127.0.0.1:8000/`.

## 📂 Project Structure

```
hospital-booking-system/
├── hospital/           # Project configuration (settings, urls, wsgi)
├── home/               # Main application app (views, models, forms)
├── Templates/          # HTML Templates
│   ├── base.html       # Base layout
│   ├── index.html      # Home page
│   ├── doctors.html    # Doctor listings
│   ├── booking.html    # Appointment form
│   └── ...
├── static/             # CSS, JS, Images
├── manage.py           # Django command-line utility
└── requirements.txt    # Project dependencies
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).
