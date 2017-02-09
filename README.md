{% comment "This comment section will be deleted in the generated project" %}

## Features

* Ready Bootstrap-themed pages
* User Registration/Sign up
* Better Security with [12-Factor](http://12factor.net/) recommendations 
* Logging/Debugging Helpers
- Production-ready configuration for Static Files, Database Settings, Gunicorn, etc.
- Enhancements to Django's static file serving functionality via WhiteNoise.
- Latest Python 3.6 runtime environment. 

## How to Use

To use this project, follow these steps:

1. Create your working environment.
2. Install Django (`$ pip install django`)
3. Create a new project using this template

## Creating Your Project

Using this template to create a new Django app is easy::

## Quick Start:

1. `$ django-admin startapp --template=https://github.com/Mr4x3/django-project-kick-starter/archive/master.zip --extension=*,py,html,env,md YOUR-APP-NAME`

__or__

- `$ django-admin startapp --template=~/Documents/django-projects/django-project-kick-starter --name=Procfile --extension=py,html,env,md YOUR-APP-NAME`


You can replace ``YOUR-APP-NAME`` with your desired project name.

2. `$ cd my_proj`
3. `$ pip install -r requirements.txt `

## Deployment to Heroku

    $ git init
    $ git add -A
    $ git commit -m "Initial commit"

    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate

See also, a [ready-made application](https://github.com/heroku/python-getting-started), ready to deploy.

## Using Python 2.7?

Just update `runtime.txt` to `python-2.7.13` (no trailing spaces or newlines!).

## Further Reading

- [Gunicorn](https://warehouse.python.org/project/gunicorn/)
- [WhiteNoise](https://warehouse.python.org/project/whitenoise/)
- [dj-database-url](https://warehouse.python.org/project/dj-database-url/)

Rest of this README will be copied to the generated project.

--------------------------------------------------------------------------------------------

{% endcomment %}

# {{ project_name | title }} #

### About ###

{{ project_name | title }} is built with [Python 3.5][0] using the [Django Web Framework 1.10][1]. This Project is _short description_.

This project has the following basic apps:

* App1 (_short description_)
* App2 (_short description_)
* App3 (_short description_)

### Notes ###

This project will be using pymysql package to be able communicate with database as official python-mysql driver do not support python 3 yet.

## Installation

### Quick start

To set up a development environment quickly, first install Python 3. It
comes with virtualenv built-in. So create a virtual env by:

    1. `$ python3 -m venv {{ project_name }}`
    2. `$ . {{ project_name }}/bin/activate`
    3. `$ create database {{ project_name }}`

Install all dependencies:

    pip install -r requirements.txt

Run migrations:

    python manage.py migrate

### Detailed instructions

Take a look at the docs for more information.

[0]: https://www.python.org/
[1]: https://www.djangoproject.com/
