## Installation

### Create an environment

Create a project folder and a `venv` folder within:

```bash=
mkdir "your folder"
cd "your folder"
python3 -m venv venv
```

On Windows:

```bash=
py -3 -m venv venv
```

### Activate the environment

```bash=
. venv/bin/activate
```

On Windows:

```bash=
venv\Scripts\activate
```

### Install Flask & packages

Within the activated environment, install dependencies:

For the first time

```bash=
pip install flask flask_sqlalchemy flask-login flask-admin
pip install flask_wtf
pip install psycopg2-binary
pip install flask-marshmallow
pip install -U marshmallow-sqlalchemy
pip install Flask-Migrate
pip install gunicorn
pip freeze > requirements.txt
```

For someone who clone the project

```bash=
pip install -r requirements.txt
```

### Run project

```bash=
flask db init
flask run
```

or

```
flask db init
python app.py
```

### Database migration

```
flask db migrate -m "Message"
flask db upgrade
```
