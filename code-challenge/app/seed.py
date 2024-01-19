from app import create_app, app
import random

from models import  db, Vendor, Sweet, VendorSweet

app = create_app()
app.app_context().push()


vendor1 = Vendor(name='Insomnia Cookies')
vendor2 = Vendor(name='Cookies Cream')

sweet1 = Sweet(name='Chocolate Chip Cookie')
sweet2 = Sweet(name='Brownie')

vendor_sweet1 = VendorSweet(price=200, vendor=vendor1, sweet=sweet1)
vendor_sweet2 = VendorSweet(price=300, vendor=vendor1, sweet=sweet2)


db.session.add_all([vendor1, vendor2, sweet1, sweet2, vendor_sweet1, vendor_sweet2])
db.session.commit()
app.app_context().pop()
