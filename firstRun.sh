source bin/activate
cd whiteboard
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata data.json
