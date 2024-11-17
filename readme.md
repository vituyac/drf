python -m venv venv
venv/scripts/activate

pip install django
pip install djangorestframework
pip install drf-spectacular

django-admin startproject core
python manage.py startapp Account

python manage.py makemigrations
python manage.py migrate