# What is This?
It's Django Cheat Sheet
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

# How the inside code works ?
- The class are used to make the section of data
- In class there is attribute that you made like question,option etc.