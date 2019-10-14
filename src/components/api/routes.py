from flask import jsonify, request
from src import db
from flask_cors import CORS
from flask import Blueprint


api_bpt = Blueprint('api', __name__)


# Init Cors
CORS(api_bpt)

# Product Routes
from src.models import Product, products_schema, product_schema  # noqa
# Create a Product
@api_bpt.route('/products', methods=['POST'])
def add_product():
    name = request.json["name"]
    onSale = request.json["onSale"]
    img_src = request.json["img_src"]
    prod_type = request.json["prod_type"]
    short_desc = request.json["short_desc"]
    price = request.json["price"]
    popupId = request.json["popupId"]
    popupImg = request.json["popupImg"]
    isAvailable = request.json["isAvailable"]
    popupCat = request.json["popupCat"]
    popupTag = request.json["popupTag"]
    popupDesc = request.json["popupDesc"]

    new_product = Product(
        name=name,
        onSale=onSale,
        img_src=img_src,
        prod_type=prod_type,
        short_desc=short_desc,
        price=price,
        popupId=popupId,
        popupImg=popupImg,
        isAvailable=isAvailable,
        popupCat=popupCat,
        popupTag=popupTag,
        popupDesc=popupDesc
    )

    db.session.add(new_product)
    db.session.commit()

    return product_schema.jsonify(new_product)

# Get All Products
@api_bpt.route('/products', methods=['GET'])
def get_products():
    all_products = Product.query.all()
    result = products_schema.dump(all_products)
    return jsonify({'products:': result})

# Get Single Products
@api_bpt.route('/products/<id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product)

# Update a Product
@api_bpt.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)

    name = request.json["name"]
    onSale = request.json["onSale"]
    img_src = request.json["img_src"]
    prod_type = request.json["prod_type"]
    short_desc = request.json["short_desc"]
    price = request.json["price"]
    popupId = request.json["popupId"]
    popupImg = request.json["popupImg"]
    isAvailable = request.json["isAvailable"]
    popupCat = request.json["popupCat"]
    popupTag = request.json["popupTag"]
    popupDesc = request.json["popupDesc"]

    product.name = name
    product.onSale = onSale
    product.img_src = img_src
    product.prod_type = prod_type
    product.short_desc = short_desc
    product.price = price
    product.popupId = popupId
    product.popupImg = popupImg
    product.isAvailable = isAvailable
    product.popupCat = popupCat
    product.popupTag = popupTag
    product.popupDesc = popupDesc

    db.session.commit()

    return product_schema.jsonify(product)

# Delete Product
@api_bpt.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)


# User Routes
from src.models import User, users_schema, user_schema  # noqa
# Create a User
@api_bpt.route('/users', methods=['POST'])
def add_user():
    gender = request.json["gender"]
    first_name = request.json["first_name"]
    last_name = request.json["last_name"]
    address = request.json["address"]
    email = request.json["email"]
    user_name = request.json["user_name"]
    dob = request.json["dob"]
    img_large = request.json["img_large"]
    img_medium = request.json["img_medium"]
    img_thumbnail = request.json["img_thumbnail"]

    new_user = User(
        gender=gender,
        first_name=first_name,
        last_name=last_name,
        address=address,
        email=email,
        user_name=user_name,
        dob=dob,
        img_large=img_large,
        img_medium=img_medium,
        img_thumbnail=img_thumbnail,
    )
    new_user.set_password(request.json["password"])
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user.data)

# Get All Users
@api_bpt.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify({'users:': result})

# # # Get Single Products
# # @api_bpt.route('/products/<id>', methods=['GET'])
# # def get_product(id):
# #     product = Product.query.get_or_404(id)
# #     return product_schema.jsonify(product)

# # # Update a Product
# # @api_bpt.route('/products/<id>', methods=['PUT'])
# # def update_product(id):
# #     product = Product.query.get_or_404(id)

# #     name = request.json["name"]
# #     onSale = request.json["onSale"]
# #     img_src = request.json["img_src"]
# #     prod_type = request.json["prod_type"]
# #     short_desc = request.json["short_desc"]
# #     price = request.json["price"]
# #     popupId = request.json["popupId"]
# #     popupImg = request.json["popupImg"]
# #     isAvailable = request.json["isAvailable"]
# #     popupCat = request.json["popupCat"]
# #     popupTag = request.json["popupTag"]
# #     popupDesc = request.json["popupDesc"]

# #     product.name = name
# #     product.onSale = onSale
# #     product.img_src = img_src
# #     product.prod_type = prod_type
# #     product.short_desc = short_desc
# #     product.price = price
# #     product.popupId = popupId
# #     product.popupImg = popupImg
# #     product.isAvailable = isAvailable
# #     product.popupCat = popupCat
# #     product.popupTag = popupTag
# #     product.popupDesc = popupDesc

# #     db.session.commit()

# #     return product_schema.jsonify(product)

# # # Delete Product
# # @api_bpt.route('/products/<id>', methods=['DELETE'])
# # def delete_product(id):
# #     product = Product.query.get_or_404(id)
# #     db.session.delete(product)
# #     db.session.commit()

# #     return product_schema.jsonify(product)
