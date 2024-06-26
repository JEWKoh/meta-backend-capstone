﻿# Getting Started with Django Project
This Django project utilizes Django REST Framework (DRF) and djoser for authentication.

## Available Scripts
In the project directory, you can run:

### Running the Development Server
To start the Django development server, run:


### `python manage.py runserver`

The development server will run at http://localhost:8000/. You can view the API endpoints in your browser or test them using tools like Postman.

### Running Tests

To launch the test runner, use:

### `python manage.py test`

This command runs all the test cases configured in your Django project.

### Building for Production

To prepare your Django project for production, you would typically focus on configuring your server environment and ensuring deployment readiness. Django projects are generally deployed using WSGI servers like Gunicorn and reverse proxies like Nginx or Apache.

### Advanced Configuration

For advanced configuration and customization, refer to the Django and Django REST Framework documentation:

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework Documentation](https://www.django-rest-framework.org/)

### Authentication and User Management
This project uses djoser for user authentication. Here are some key endpoints provided by djoser:

* Registration: /auth/users/
* Login: /auth/token/login/
* Logout: /auth/token/logout/

Ensure to customize and secure these endpoints based on your project's requirements and security policies.

### Learn More
You can learn more about Django and Django REST Framework through their official documentation:

* [Django Documentation](https://docs.djangoproject.com/en/stable/)
* [Django REST Framework Documentation](https://www.django-rest-framework.org/)

### Troubleshooting

If you encounter issues specific to Django or Django REST Framework, refer to their troubleshooting guides:

* [Django Troubleshooting](https://docs.djangoproject.com/en/stable/topics/faq/)
