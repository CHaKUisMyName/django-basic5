# Description

django project playground use python 3.13.1 pyenv venv bootstrap5, project is CRUD mock data

- login system check session form client and DB
- create middleware injection for get current_user
- create decorator @custom_is_login for check login befor request method
- create {% load custom_tags %} for get email user login display in layout

# Install

- install python 3.13.1
- install pyenv
- use pyenv python version
- create venv
- activate venv
- pull this project branch main
- install lib

```
pip install -r requirements.txt
```

- run project

```
python manage.py runserver
```
