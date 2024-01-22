from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Vendor, Sweet, VendorSweet
from flask_restful import Resource, Api, reqparse

db = SQLAlchemy()
migrate = Migrate()
api = Api()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)


    return app

app = create_app()

parser = reqparse.RequestParser()
parser.add_argument('price', type=int, required=True, help='Price is required and must be an integer')
parser.add_argument('vendor_id', type=int, required=True, help='Vendor ID is required and must be an integer')
parser.add_argument('sweet_id', type=int, required=True, help='Sweet ID is required and must be an integer')

class VendorResource(Resource):
    def get(self):
        vendors = Vendor.query.all()
        response = [vendor.to_dict() for vendor in vendors]
        return response

class VendorByIdResource(Resource):
    def get(self, vendor_id):
        vendor = Vendor.query.get(vendor_id)
        if vendor is None:
            return {"error": "Vendor not found"}, 404

        return vendor.to_dict()
    
class SweetsResource(Resource):
    def get(self):
        sweets = Sweet.query.all()
        response = [sweet.to_dict() for sweet in sweets]
        return response

class SweetByIdResource(Resource):
    def get(self, sweet_id):
        sweet = Sweet.query.get(sweet_id)
        if sweet is None:
            return {"error": "Sweet not found"}, 404

        return sweet.to_dict()
    
class VendorSweetsResource(Resource):
    def post(self):
        args = parser.parse_args()

       
        vendor = Vendor.query.get(args['vendor_id'])
        sweet = Sweet.query.get(args['sweet_id'])

        if vendor is None or sweet is None:
            return {'error': 'Invalid vendor_id or sweet_id'}, 400

        vendor_sweet = VendorSweet(
            vendor_id=args['vendor_id'],
            sweet_id=args['sweet_id'],
            price=args['price']
        )

        db.session.add(vendor_sweet)
        db.session.commit()

        response = {
            'id': vendor_sweet.id,
            'name': sweet.name,  
            'price': vendor_sweet.price
        }

        return response, 201
class VendorSweetResource(Resource):
    def delete(self, vendor_sweet_id):
        vendor_sweet = VendorSweet.query.get(vendor_sweet_id)

        if vendor_sweet:
            db.session.delete(vendor_sweet)
            db.session.commit()
            return {"message": f"VendorSweet with ID {vendor_sweet_id} successfully deleted"}, 200 
        else:
            return {"error": "VendorSweet not found"}, 404  
    

    
api.add_resource(VendorSweetResource, '/vendor_sweets/<int:vendor_sweet_id>')
api.add_resource(VendorResource, '/vendors')
api.add_resource(VendorByIdResource, '/vendors/<int:vendor_id>')
api.add_resource(SweetsResource, '/sweets')
api.add_resource(SweetByIdResource, '/sweets/<int:sweet_id>')
api.add_resource(VendorSweetsResource, '/vendor_sweets')


if __name__ == '__main__':
    app.run(port=5555)