from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Vendor(db.Model):
    __tablename__ = 'vendor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='vendor')

class Sweet(db.Model):
    __tablename__ = 'sweet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    vendor_sweets = db.relationship('VendorSweet', back_populates='sweet')

class VendorSweet(db.Model):
    __tablename__ = 'vendor_sweets'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'), nullable=False)
    sweet_id = db.Column(db.Integer, db.ForeignKey('sweet.id'), nullable=False)
    vendor = db.relationship('Vendor', back_populates='vendor_sweets')
    sweet = db.relationship('Sweet', back_populates='vendor_sweets')
