web: gunicorn course_project.wsgi --bind=0.0.0.0:$PORT
heroku ps:scale web=1
release: python manage.py migrate