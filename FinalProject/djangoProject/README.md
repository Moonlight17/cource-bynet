[![license](https://img.shields.io/github/license/mashape/apistatus.svg)]()

# Backend
The application wrote on python with framework Django4

### For start backend's application you need run next steps

Activate Virtual Enviroment:
```bash
source ./venv/bin/activate
```
Create migrations and apply it into DataBase:
```bash
python manage.py makemigrations             # system's migrations 
python manage.py makemigrations aggregated  # appliaction's migrations

python manage.py migrate                # applying system's tables
python manage.py migrate aggregated     # applying application's tables
```

Last step - run server
``` bash
python manage.py runserver # by default using 8000 port, but you can overwrite it python manage.py runserver 8000

```


# Urls

## GET
```' ' ``` - Life check (returned only status 200 for checking health)

```'init/' ``` - Adding data by default

```'files/' ``` - It's method for cyclically executed

```'participants/' ``` - Download information about attendance for all Participants

## POST
``` 'aggregate/31-12-2021/31-12-2022' ``` - Download information about attendance for all on the specified dates

``` need ``` - parametrs for get information only about the necessary visitors
