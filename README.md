# README #

This project has been developed to help Iniciador to manage the community in
the long term.

### How do I get set up? ###

Follow those steps in order to be able to execute this project in local:

1) (Optional) Create a local isolated environment

```
virtualenv iniciador
source ./iniciador/bin/activate
```

2) Install the dependencies executing:

```
pip install -r requirements.txt
```
3) Run the developement server like this:

```
python manage.py runserver
```

4) Then open a browser on: http://localhost:80000

### Who do I talk to? ###

* Raul Jimenez Ortega (hhkaos@gmail.com)
* Gerencia@iniciador.com

### Pending tasks ###

* Change media files -> http://django-storages.readthedocs.org/en/latest/backends/apache_libcloud.html
* Validate signup form & placeholders & info (frontend) - usuarios duplicados, correos ya registrados, etc.
* Prepare page that list all members
* Finish homepage
* Prepare automatic emails (every day)
  * If (last_activity = 60 days) -> send mail to update_last activity & check profile
  * If (last_activity = 75 day) -> notify admins
* Add current members
* Add cron task (check if member is still active), after 60 days of his last activity, if not -> send email thought mandril to check
* Si el nombre de usuario ya existe crear buscar otro
* Enviar mail para notificar la solicitud de nueva alta de miembro/grupo
* Estado de grupos pendientes/miembros, solicitar nuevo grupo.
