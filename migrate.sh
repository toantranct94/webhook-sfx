cd registration-service
export FLASK_APP=./app/app.py
export FLASK_ENV=local

flask db migrate
flask db upgrade
