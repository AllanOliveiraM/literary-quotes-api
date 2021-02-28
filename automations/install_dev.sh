echo '>> Generating a VEnv instance and activating...'
python3 -m venv venv
source venv/bin/activate

echo '>> Installing python dependencies...'
pip install -r requirements/requirements-dev.txt

echo '>> Clearing Sqlite3 local database...'
rm db.sqlite3

echo '>> Creating database local migrations...'
python manage.py migrate

echo '>> Running development server in localhost:8000...'
python manage.py runserver
