import os
from flask import Flask, request, jsonify
# from flask import Flask, redirect, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# from flask_admin import Admin
# from flask_login import LoginManager, current_user

# init app
app = Flask(__name__)

# config
app.config['SECRET_KEY'] = os.environ['MY_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

# Init db
db = SQLAlchemy(app)
# Init ma
ma = Marshmallow(app)


# Product Schema


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@app.route('/')
def index():
    return jsonify({'ecomCDS': 'home'})

# Create a Product
@app.route('/api/products', methods=['POST'])
def add_product():
    name = request.json["name"]
    description = request.json["description"]
    price = request.json["price"]
    qty = request.json["qty"]

    new_product = Product(
        name=name, description=description, price=price, qty=qty)

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get All Products
@app.route('/api/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify({'products:': result})

# Get Single Products
@app.route('/api/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
@app.route('/api/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)

    name = request.json['name']
    description = request.json['description']
    price = request.json['price']
    qty = request.json['qty']

    product.name = name
    product.description = description
    product.price = price
    product.qty = qty

    db.session.commit()

    return product_schema.jsonify(product)

# Delete Product
@app.route('/api/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


# Run Server
if __name__ == '__main__':
    app.run(debug=True)
