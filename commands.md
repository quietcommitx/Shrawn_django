# Install Virtual Environment
pip install virtualenv

# Create a virtual environment         - for every project
python -m venv virtualenv_name
python -m venv venv/env/BDC
or
virtualenv virtualenv_name
virtualenv env/venv/abc

# activate virtual environment
env\Scripts\activate          [Win]
source env/Scripts/activate   [IOS, linux]

# deactivate virtual environment
deactivate

# install DJango
pip install django

# project create
django-admin startproject project_name .        ['.' is optional]

# start app
python manage.py startapp app_name


# Django Architecture
## MVT Aechitecture
### M: Model
- database, table, fields, datatype
### V: View
- logics, data manipulation, communication with url, models and template
### T: Template
- user interface, frontend, html, css, js
