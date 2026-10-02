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



ORM: Object Relational Mapping 
- way to interact with database using programming language objects/classes instead of sql directly

sql: SELECT * FROM NOTE;      # Get all data from NOTE table
SELECT * FROM NOTE where id = 15;    # get all data from NOTE table whose title is writing

# CRUD operation: Create, Retrieve, Update, Delete
# Get all data from a table
ORM: model_name/table_name.objects.all()
model_name/table_name.objects.all().values()

# add/create data 
model_name.objects.create(field1="....", field2=".....", field3 = "....", .......)
Note.objects.create(title="first",content="this is the first note",created_at=2026-09-28)

# Retrieve: access/get/fetch single data
a = model_name.objects.get(id = 1)

# Update:
a.title = "New data"
a.field1 = "...."
a.field2 = "...."
a.save()

# Delete:
a.delete()

# filter
model_name.objects.filter(title="something", field1 ="...", field3 = "...")

# create/update requirements.txt
pip freeze > requirements.txt

# install or uninstall requirements file
pip install -r requirements.txt
pip uninstall -r requirements.txt