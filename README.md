# README #

This project has been developed to help Iniciador to manage the community in
the long term.

### Requirements ###

1) Postgre SQL
apt-get update
sudo apt-get install postgresql postgresql-contrib postgresql-server-dev-9.3

sudo apt-get install python-dev
sudo apt-get install libevent-dev
apt-get install libreadline-gplv2-dev
apt-get install libncurses5-dev


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

Trello Dashboard: https://trello.com/b/ATrPZcL8/reiniciador-website
