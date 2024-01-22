from app import app
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from models import  db, Vendor, Sweet, VendorSweet



with app.app_context():

    vendors = [
        {'name': 'Sweet Haven'},
        {'name': 'Candy Creations'},
        {'name': 'Sugar Paradise'},
        {'name': 'Tasty Treats'},
        {'name': 'Delightful Delights'},
        {'name': 'Flavorful Fantasy'},
        {'name': 'Sweets Emporium'},
        {'name': 'Heavenly Sweets'},
        {'name': 'Gourmet Goodies'},
        {'name': 'Yummy Yums'},
        {'name': 'Sugar Rush'},
        {'name': 'Divine Confections'},
        {'name': 'Mega Sweets'},
        {'name': 'Sweet Symphony'},
        {'name': 'Fantastic Flavors'},
        {'name': 'Epicurean Delights'},
        {'name': 'Wholesome Goodies'},
        {'name': 'Joyful Treats'},
        {'name': 'Luscious Sweets'},
        {'name': 'Sweet Elegance'},
    ]

    sweets = [
        {'name': 'Choco Bliss'},
        {'name': 'Fruit Fusion'},
        {'name': 'Caramel Delight'},
        {'name': 'Mango Tango'},
        {'name': 'Cookie Carnival'},
        {'name': 'Fruity Fantasy'},
        {'name': 'Velvet Delight'},
        {'name': 'Honey Heaven'},
        {'name': 'Peach Paradise'},
        {'name': 'Citrus Burst'},
        {'name': 'Crunchy Caramel'},
        {'name': 'Cherry Delight'},
        {'name': 'Mint Madness'},
        {'name': 'Toffee Temptation'},
        {'name': 'Butterscotch Bliss'},
        {'name': 'Coconut Craze'},
        {'name': 'Almond Delight'},
        {'name': 'Raspberry Rapture'},
        {'name': 'Blueberry Bliss'},
        {'name': 'Hazelnut Harmony'},
    ]

    vendor_sweets = [
        {'vendor_id': 1, 'sweet_id': 1, 'price': 220},
        {'vendor_id': 1, 'sweet_id': 2, 'price': 320},
        {'vendor_id': 2, 'sweet_id': 3, 'price': 260},
        {'vendor_id': 2, 'sweet_id': 4, 'price': 190},
        {'vendor_id': 3, 'sweet_id': 5, 'price': 230},
        {'vendor_id': 3, 'sweet_id': 6, 'price': 370},
        {'vendor_id': 4, 'sweet_id': 7, 'price': 300},
        {'vendor_id': 4, 'sweet_id': 8, 'price': 220},
        {'vendor_id': 5, 'sweet_id': 9, 'price': 320},
        {'vendor_id': 5, 'sweet_id': 10, 'price': 250},
        {'vendor_id': 6, 'sweet_id': 11, 'price': 280},
        {'vendor_id': 6, 'sweet_id': 12, 'price': 340},
        {'vendor_id': 7, 'sweet_id': 13, 'price': 190},
        {'vendor_id': 7, 'sweet_id': 14, 'price': 320},
        {'vendor_id': 8, 'sweet_id': 15, 'price': 270},
        {'vendor_id': 8, 'sweet_id': 16, 'price': 300},
        {'vendor_id': 9, 'sweet_id': 17, 'price': 240},
        {'vendor_id': 9, 'sweet_id': 18, 'price': 340},
        {'vendor_id': 10, 'sweet_id': 19, 'price': 300},
        {'vendor_id': 10, 'sweet_id': 20, 'price': 220},
    ]

    for vendor_data in vendors:
        vendor = Vendor(**vendor_data)
        db.session.add(vendor)

    db.session.commit()
    print("🍭 Vendor has been seeded!")

    for sweet_data in sweets:
        sweet = Sweet(**sweet_data)
        db.session.add(sweet)

    db.session.commit()
    print("🍬 Sweet seeded!")

    for vs_data in vendor_sweets:
        vendor_sweet = VendorSweet(**vs_data)
        db.session.add(vendor_sweet)

    db.session.commit()
    print("🍭 VendorSweets seeded!")
