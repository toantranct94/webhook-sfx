cd registration-service
export FLASK_APP=app
export FLASK_ENV=local

flask db init
flask db migrate
flask db upgrade
