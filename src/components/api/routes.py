from flask import jsonify, request
from src import db
# from src.components.api.blueprint import api_bpt
from flask_cors import CORS
from flask import Blueprint

api_bpt = Blueprint('api', __name__)
# Init Cors
CORS(api_bpt)


# Product Routes ********************************Product Routes ***********************Product Routes*****
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
    return jsonify({'products': result})

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
# /Product Routes ********************************/Product Routes ***********************/Product Routes*****


# **** User Routes**************************** User Routes************************User Routes
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

    return user_schema.jsonify(new_user)

# Get All Users
@api_bpt.route('/users', methods=['GET'])
def get_users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify({'users': result})


# purchase routes************

# Call this route when buying items (e.g. creating a purchase).
# Input API parameters:
# buyer_id - id of the user buying
# cart_items - an array of objects, representing each line item from the cart.
#              each object holds a quantity and a product_id.
#
# Example:
# POST /purchases
# {
#    buyer_id: 3,
#    cart_items: [
#        { qty: 2, product_id: 5 },
#        { qty: 1, product_id: 8 },
#        { qty: 1, product_id: 9 }
#    ]
# }
# Returns:
# JSON Object representing purchase, plus a total amount
# Example:
# {
#     purchase: { ... }
#     total: 120000
# }
from src.models import Purchase, purchases_schema, purchase_schema  # noqa
from src.models import P_Item, purchase_items_schema, purchase_item_schema  # noqa

# Add Purchase
@api_bpt.route('/purchases', methods=['POST'])
def add_purchase():
    buyer_id = request.json["buyer_id"]
    new_purchase = Purchase(
        buyer_id=buyer_id,
        status_id=1
    )
    # commit new_purchase to database to get purchase id
    db.session.add(new_purchase)
    db.session.commit()

    # This is placeholder code so we can test.
    # cart_items = request.json["cart_items"]
    # return jsonify({
    #     "purchase": {
    #         "buyer_id": buyer_id,
    #         "items": cart_items,
    #         "test": cart_items[0]['qty']
    #     },
    #     "total": 1250
    # })

    cart_items = request.json["cart_items"]
    # add purchase_items to new_purchase
    for item in cart_items:
        new_p_item = P_Item(
            qty=item['qty'],
            product_id=item['product_id'],
            purchase_id=new_purchase.id
        )
        db.session.add(new_p_item)

    new_purchase.total = new_purchase.set_total()
    db.session.add(new_purchase)
    # commit both purchase item and purchase total to db.
    db.session.commit()

    # return purchase
    resp = purchase_schema.dump(new_purchase)
    return jsonify({'msg': 'Your purchase was received', 'purchase': resp})

# Get All Purchases
@api_bpt.route('/purchases', methods=['GET'])
def get_purchase():
    all_purchases = Purchase.query.all()
    result = purchases_schema.dump(all_purchases)
    return jsonify({'purchases': result})
