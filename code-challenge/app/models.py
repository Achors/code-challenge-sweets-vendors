from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin


db = SQLAlchemy()

class Vendor(db.Model, SerializerMixin):
    __tablename__ = 'vendor'

    serialize_rules = ('-vendor_sweets.vendor',)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='vendor')
    create_at=db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    update_at=db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class Sweet(db.Model, SerializerMixin):
    __tablename__ = 'sweet'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='sweet')
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

class VendorSweet(db.Model, SerializerMixin):
    __tablename__ = 'vendor_sweets'

    serialize_rules = ('-vendor', '-sweet')

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    vendor = db.relationship('Vendor', back_populates='vendor_sweets')
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)



@db.validates('price')
def validate_price(self,key,price):
    if not price:
        raise ValueError('Price cannot be blank')
    if price<0:
        raise ValueError("Price can't be negative number")
    return price