# Django Cheat Sheet
This is my version of Django Cheat Sheet. This app are pollster app. It used to make polls.
# How you build this?
So to build this
- Install python
- Install virtual environment
> pip install pipenv
- Access virtual environment shell
> pipenv shell
- Install django using pipenv
> pipenv install django
- Use this command to initialize django
> django-admin startproject name-of-project

# What's inside?
- #### manage.py
    - to manage migration. Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema
- #### __init__.py
    - 
- #### asgi.py
    - 
- #### settings.py
    - 
- #### urls.py
    - Routes file. Managing project page. It used to link the App, give some section the link, and in main directory, it used to connect url inside the app directory to main directory.
- #### wsgi.py
    - 

# What files you will frequently modify?

## In Main
- urls.py
- settings.py
- manage.py

## In App
- models.py
- views.py
- admin.py
- urls.py
- apps.py


# How to run it?
In the pipenv shell
> python manage.py runserver PORT
Ex:
> python manage.py runserver 8000

# How to make the apps?
> python manage.py startapp name-of-app

# What difference between Project and Apps?
What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.

# What inside the apps?
- #### migrations
    - Set of folder uses for migration
- #### admin.py
    - the admin page. in this folder we can register our model to show it on admin page and we can peek and modified it
- #### apps.py
    - 
- #### models.py
    - the backend workfile. it manage data like option, choice, question, etc
- #### tests.py
    - the test file. it used to make some test file so other user can sandboxing the model
- #### view.py
    - It manage front-end of website, the admin otherhands

# How to make basic apps in nutshell?
- Make the models in models.py
- Register the models in admin.py
- import html template in views.py
- make urls.py inside the app and import all views.py function to insert html template page
- add apps.py inside the settings.py in ***INSTALLED APPS*** variable 
    - the format is '<app-name>.apps.<Appname>Config'
- import os inside settings.py if not imported by default
- add template directory in ***TEMPLATE*** variable
    - add this in **DIR** keys 
    ```python
        TEMPLATE = {......
                    'DIRS':[os.path.join(BASE_DIR,'<template-path>')]
                    .....
                    }
    ```
- make migration
```cmd
python manage.py makemigrations 
```
- migrate the model to database
```cmd
python manage.py migrate 
```
- run the server
```cmd
python manage.py runserver
```

# Django Template programming

***Folder hierarchy***
```
└───public
        ├───nothing
        │       file.html
        │
        └───polls
                index.html
                result.html
```

***This will create local template called somt (for now, treat it as file.html)***
```html
<!-- in file.html -->
{% block somt %}
{% endblock %}
```

***This will extract html file(in this example it will) and add 'something' in block called 'somt'***
```html
<!-- in polls/index.html -->
{% extend 'nothing/file.html' %}

{% block somt %}
    Something
{% endblock %}
```

