from flask_login import UserMixin, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from src import db, ma, admin_mgr
from flask_admin.contrib.sqla import ModelView
from datetime import datetime


# purchase_item Class/Model *************  # purchase_item Class/Model*******


class P_Item(db.Model):
    __tablename__ = 'p_item'
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), default=1, nullable=False)
    purchase_id = db.Column(db.Integer, db.ForeignKey(
        'purchase.id'), default=1, nullable=False)
    qty = db.Column(db.Float, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"p_item id:{self.id} - purchase id - {self.purchase_id} - product id: {self.product_id}."

# purchase_item Schema


class purchase_itemSchema(ma.ModelSchema):
    class Meta:
        model = P_Item


# Init purchase_item schema
purchase_item_schema = purchase_itemSchema()
purchase_items_schema = purchase_itemSchema(many=True)


# Product Class/Model ********* # Product Class/Model *************


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    saler_id = db.Column(db.Integer, db.ForeignKey('user.id'), default=1)
    name = db.Column(db.String(100), unique=True)
    onSale = db.Column(db.Boolean)
    img_src = db.Column(db.String)
    prod_type = db.Column(db.String)
    short_desc = db.Column(db.Text)
    price = db.Column(db.String)
    popupId = db.Column(db.String)
    popupImg = db.Column(db.String)
    isAvailable = db.Column(db.Boolean)
    popupCat = db.Column(db.String)
    popupTag = db.Column(db.String)
    popupDesc = db.Column(db.Text)
    isActive = db.Column(db.Boolean, default=True)
    created_date = db.Column(db.DateTime, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now)
    purchase_items = db.relationship(
        "P_Item", backref="product", lazy="dynamic")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"product {self.id} - {self.name}."

# Product Schema


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'onSale', 'img_src', 'prod_type', 'short_desc', 'price',
                  'popupId', 'popupImg', 'isAvailable', 'popupCat', 'popupTag', 'popupDesc')


# Init prduct schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


# User Model*******# User Model*******# User Model***
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    address = db.Column(db.String)
    email = db.Column(db.String(120), index=True, unique=True)
    user_name = db.Column(db.String(80), nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    dob = db.Column(db.DateTime)
    img_large = db.Column(db.String)
    img_medium = db.Column(db.String)
    img_thumbnail = db.Column(db.String)
    created_date = db.Column(
        db.DateTime, nullable=False, default=datetime.utcnow)
    updated_date = db.Column(
        db.DateTime,  nullable=False, default=datetime.utcnow)
    isSaler = db.Column(db.Boolean, default=False)
    isAdmin = db.Column(db.Boolean, default=False)
    isActive = db.Column(db.Boolean, default=True)
    products = db.relationship("Product", backref="user", lazy="dynamic")
    purchases = db.relationship("Purchase", backref="user", lazy="dynamic")

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"{self.id} user_name is {self.user_name}."

# User Schema


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'onSale', 'img_src', 'prod_type', 'short_desc', 'price', 'popupId', 'popupImg', 'isAvailable', 'popupCat', 'popupTag', 'popupDesc'
                  )


# Init User schema
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# Purchase Class/Model *************# Purchase Class/Model*********# Purchase Class/Model**********


class Purchase(db.Model):
    __tablename__ = 'purchase'
    id = db.Column(db.Integer, primary_key=True)
    status_id = db.Column(db.Integer, db.ForeignKey(
        'purchase_status.id'), default=1, nullable=False)
    buyer_id = db.Column(db.Integer, db.ForeignKey(
        'user.id'), default=1, nullable=False)
    total = db.Column(db.Float, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now, nullable=False)
    updated_date = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
    purchase_items = db.relationship(
        "P_Item", backref="purchase", lazy="dynamic")

# TODO keep track of time when status change to determine timelapse between status. 

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"Purchase {self.id} - Buyer:{self.buyer_id}."

    # calculate total of order
    def set_total(self):
        amt = 0
        for item in self.purchase_items:
            amt = amt + float(item.product.price)*item.qty
        return amt

# Purchase Schema


# class PurchaseSchema(ma.ModelSchema):
#     class Meta:
#         model = Purchase
class PurchaseSchema(ma.Schema):
    class Meta:
        fields = ('id', 'buyer_id', 'created_date', 'updated_date',
                  'status_id', 'total')


# Init purchase schema
purchase_schema = PurchaseSchema()
purchases_schema = PurchaseSchema(many=True)


# Purchase_status Class/Model *************# Purchase_status Class/Model*********# Purchase_status Class/Model**********


class Purchase_status(db.Model):
    __tablename__ = 'purchase_status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_date = db.Column(db.DateTime, default=datetime.now)
    updated_date = db.Column(db.DateTime, default=datetime.now)
    isActive = db.Column(db.Boolean, default=True)
    purchase_statuses = db.relationship(
        "Purchase", backref="purchase_status", lazy="dynamic")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"Purchase_status : {self.name}."


# Purchase_status Schema


class Purchase_statusSchema(ma.ModelSchema):
    class Meta:
        model = Purchase_status


# Init purchase_status schema
purchase_status_schema = Purchase_statusSchema()
purchase_statuses_schema = Purchase_statusSchema(many=True)


# Init admin view

admin_mgr.add_view(ModelView(User, db.session))
admin_mgr.add_view(ModelView(Product, db.session))
admin_mgr.add_view(ModelView(Purchase, db.session))
admin_mgr.add_view(ModelView(P_Item, db.session))
admin_mgr.add_view(ModelView(Purchase_status, db.session))
