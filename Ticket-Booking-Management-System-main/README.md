#  Ticket Booking Management System
##  Screenshots  
_Showcase your UI here with screenshots!_  
![Screenshot 2025-04-25 110554](https://github.com/user-attachments/assets/fafcf0f7-6a3d-4c9c-b486-c963c0339930)
![Screenshot 2025-04-25 110356](https://github.com/user-attachments/assets/9aeea42f-66e7-4972-9a52-d9f31879ac9f)
![Screenshot 2025-04-25 110408](https://github.com/user-attachments/assets/e08e89e3-fb5b-4c14-8bb2-e44e23af8190)
![Screenshot 2025-04-25 110420](https://github.com/user-attachments/assets/b0495f30-d35f-4f4e-b78e-0f864a3243ae)
![Screenshot 2025-04-25 110453](https://github.com/user-attachments/assets/2e850ffc-f980-4442-b4b6-7d9637c64ad2)
![Screenshot 2025-04-25 110513](https://github.com/user-attachments/assets/f4ba0d07-600d-44e2-8c16-d8b2c61b7da4)
![Screenshot 2025-04-25 110545](https://github.com/user-attachments/assets/7bcac465-8d30-417b-b16c-ce4d38ae4f62)
![Screenshot 2025-04-25 110554](https://github.com/user-attachments/assets/30d780b7-f52e-4bcf-b620-4c18b3bec197)


##  Project Overview  
This Ticket Booking Management System is a web application built with **Django** that allows users to browse available shows, book tickets, and view their booking history. It also features an admin panel for managing shows and users.

---

##  Features

###  User Features
-  **Authentication System**: Register, login, and logout  
-  **Show Browsing**: View list of available shows with details  
-  **Ticket Booking**: Select and book tickets for available shows  
-  **Booking History**: View all past bookings  

###  Admin Features
-**Show Management**: Add, edit, and delete shows  
-  **Booking Overview**: View all bookings  
-  **User Management**: Manage user accounts  

---

##  Tech Stack
- **Backend Framework**: Django (Python)  
- **Database**: MySQL  
- **Containerization & CI/CD**: Docker, Jenkins (configured)

---



---

##  Setup Instructions

###  Prerequisites
- Python 3.8+  
- MySQL  
- Git  

---

##  Manual Setup 

###  Clone the repository

```bash
git clone https://github.com/yourusername/ticket-booking.git
cd ticket-booking
```
Create and activate a virtual environment
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
 Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
 Configure MySQL Database
Create a MySQL database named ticket_booking

Update config/settings.py with your database credentials:

python
Copy
Edit
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ticket_booking',
        'USER': 'your_mysql_user',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
 Run migrations
bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
 Create a superuser
bash
Copy
Edit
python manage.py createsuperuser
Follow the prompts to create your admin user.

 Run the development server
bash
Copy
Edit
python manage.py runserver
 Access the application
Main App: http://localhost:8000

Admin Panel: http://localhost:8000/admin/dashboard/

 User Guide
For Regular Users
 Registration: Sign up with email and password

 Browse Shows: View available shows

 Show Details: Click to explore more

 Book Tickets: Select number of seats and confirm
View Bookings: Check your booking history

For Administrators
 Admin Access: Login via admin credentials

 Manage Shows: Add, edit, delete show details

 View All Bookings: Monitor system-wide ticket bookings

 User Management: Control user accounts

 Project Structure
bash
Copy
Edit
ticket_booking/
├── config/               # Django project settings
├── accounts/             # User authentication app
├── booking/              # Core booking functionality
├── admin_panel/          # Admin management interface
├── templates/            # HTML templates
├── Dockerfile            # Docker configuration (optional)
├── docker-compose.yml    # Docker Compose (optional)
├── Jenkinsfile           # Jenkins pipeline (optional)
└── requirements.txt      # Python dependencies
