# ackerland
Python implementation of website of ackerland festival 2023 using Django framework.

## Installation
### Linux

Set up git authentification code. See: https://stackoverflow.com/a/68781050/16088612

Pull repository using git:
```sh
$ git clone https://github.com/richtercl98/ackerland-django.git ackerland
```

Ensure  system is updated and the required packages installed. 
````sh
$ sudo apt update && sudo apt upgrade -y
````

Install requirements using pip:
```sh
$ pipenv install 
```

Apply Django migrations:
```sh
$ pipenv run python manage.py makemigrations
$ pipenv run python manage.py migrate
```

Create new local django admin user:
```sh
$ pipenv run python manage.py createsuperuser
$ ...
```

Run Django Server:
```sh
$ pipenv run python manage.py runserver
```

If error `sh RuntimeError: populate() isn't reentrant` go to location of virtualenv:
```sh
$ cd ~/.local/share/virtualenvs/ackerland-django-VIRTUAL_ENV_NAME/lib/python/site-packages/django/apps
```
Open File `sh registry.py` around line 80 and replace:
```sh
raise RuntimeError("populate() isn't reentrant")
```
with:
```sh
self.app_configs = {}
```
Now real Error description will appear or its 'fixed' :)


## Usage
### Django admin Interface
New Model instances can be created easily in the admin interface provided by Django. Just visit [ localhost:8000/admin/ ] in your browser.

### Available sites
Timetable of all Floors will be availabe at [ localhost:8000/timeline/ ] .
