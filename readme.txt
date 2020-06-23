Cookify is a webapp that allows the admin to show, create and edit recipes. It uses default django admin panel to do it
(you can also POST it via REST api), frontend communicates with the backend by REST api and
it is responsive to mobile

to set up django server (on windows) navigate to main directory and enter in command line

creating venv (optional)

py -m venv env
.\env\Scripts\activate

pip install Django
pip install djangorestframework
pip install django-cors-headers
pip install Pillow
python manage.py migrate
python manage.py createsuperuser, enter credentials
python manage.py runserver

than you can add some recipes by logging in at admin panel with your credentials, default address: http://127.0.0.1:8000/admin

in order to open frontend you have to navigate to frontend/cookify

npm install
npm start

contact page and navbar will be available without adding any recipes. in order to show the full potential of app
it is advised to add at least 7 categories with at least 7 recipes in one of them
as the app sorts them basing on views anddisplays maximum of 3 recipes and 6
categories on the main page, and 6 recipes when you enter specific category

views and likes (clicking on like icon on detailed recipe page) are being registered

Warning: in order to add fully working recipe, you have to create 
category, recipe and then add step ingredients (consisting of ingredients) and step instructions linked to this recipe
photos are looking best when they are horizontally oriented

