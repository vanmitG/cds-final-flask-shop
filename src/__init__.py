import os
from datetime import datetime
# from flask import Flask, jsonify, request,
from flask import Flask, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_admin import Admin
from flask_cors import CORS

# from flask_login import LoginManager, current_user


# init app
app = Flask(__name__)

# config
app.config['SECRET_KEY'] = os.environ['MY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)
# Init migration
migrate = Migrate(app, db)
# Init Admin
admin_mgr = Admin(app, template_mode='bootstrap3')
# Init Cors
# CORS(app, resources={r"/api/*": {"origins": "*"}})

# route for sites
@app.route('/')
def index():
    return jsonify({'ecomCDS': 'home'})


@app.route('/admin')
def admin():
    return redirect(url_for('admin'))


# api blue print
from src.components.api.routes import api_bpt  # noqa
app.register_blueprint(api_bpt, url_prefix='/api')

# Init Cors
# CORS(api_bpt)
