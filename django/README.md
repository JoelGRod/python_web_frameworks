# Introduction
Django Projects folder

Author: Joel Glez Rod

## Notes
* TODO

## Instructions
* python3 -m venv venv
* . venv/bin/activate -> Accept integrate venv with your IDE
* pip3 install -r requirements.txt
* Create a new Django project: django-admin startproject todoapp
* Run a Django project:
    * cd django_app
    * python3 manage.py runserver
* Create a new Django component / app (domain module): 
    * python3 manage.py startapp todolist
    * Add component at django_app settings.py
    * Create templates folder and add it to settings.py
    * Create urls and add it to main urls
    * Create views
    * Create models
    * Create migrations: python3 manage.py makemigrations
    * python3 manage.py migrate
    * Register models in admin.py
    * Import models at places you need them
* Create super user for admin panel: python3 manage.pycreatesuperuser
* Enter into Admin Panel: https:.../admin





# Scripts and Tests
* chmod +x scripts/run_dev.sh
* ./scripts/run_dev.sh