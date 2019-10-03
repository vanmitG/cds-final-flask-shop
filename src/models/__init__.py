from src import db
from src import ma
from datetime import datetime

# Product Class/Model


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def __repr__(self):
        return f"product {self.id} - {self.name}."

# Product Schema


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'onSale', 'img_src', 'prod_type', 'short_desc', 'price', 'popupId', 'popupImg', 'isAvailable', 'popupCat', 'popupTag', 'popupDesc'
                  )


# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)
