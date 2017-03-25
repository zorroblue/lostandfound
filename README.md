# Lost&amp;Found API for Inter IIT Tech Meet 2017

## What is it?

This is a Django based REST API for handling the Lost & Found submodule for Inter IIT Tech Meet 2017.

## Features
This API has endpoints which allow you to:

1. Create new notices
2. Delete notices you created
3. Update a notice you created
4. View the noticeboard

The code has been modified to host on a heroku host directly

## Running the code on a local system

1. Install requirements `pip install -r requirements.txt`
2. Comment out lines for DATABASES in settings.py and uncomment the previous definition for DATABASES. (needed to access local database)
3. Run the server `python manage.py runserver`

Each API endpoint returns a JSON response.
