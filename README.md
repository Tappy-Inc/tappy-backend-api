# tappy-backend-api

This is the backend API for the Tappy project. Follow the instructions below to set up the project.

## Setup

1. Install Django:
```pip install Django```

2. Start the Django project:
```django-admin startproject tappy .```

3. Start the Django app:
```python manage.py startapp tappy_app```

## Dependencies

The following packages are required for this project:

1. django-environ:
```pip install django-environ```

2. django-log-request-id:
```pip install django-log-request-id```

3. psycopg2:
```pip install psycopg2```

4. djangorestframework-simplejwt:
```pip install djangorestframework-simplejwt```

5. drf-yasg:
```pip install drf-yasg```

6. django-cors-headers:
```pip install django-cors-headers```

Install all dependencies at once by running:
```pip install -r requirements.txt```

## Running the server

To run the server, use the following command:
```python manage.py runserver```

## Additional Setup

Create a new directory and start a new Django app:
```mkdir domain/user && python manage.py startapp user domain/user```

## TODO

- [x] Work Schedule related to User (All Type of Users)
- [x] Work Information related to User (Position, Client, Compensation package, )
- [x] Work History - employee work history (Promotion history)
- 


```javascript
fetch('https://api.tappy.com.ph/authentication/session/', {
  method: 'GET',
  credentials: 'include',
  headers: {
    'accept': 'application/json',
  }
}).then(response => response.json())
  .then(data => console.log(data))
  .catch((error) => console.error('Error:', error));
```