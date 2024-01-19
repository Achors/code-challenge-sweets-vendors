from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Vendor, Sweet, VendorSweet

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from models import Vendor, Sweet, VendorSweet

    # Import and register blueprints, if any
    # from .blueprints import some_blueprint
    # app.register_blueprint(some_blueprint)

    return app


app = create_app()
migrate = Migrate(app, db)




@app.route('/')
def home():
    return ''

if __name__ == '__main__':
    app.run(port=5555)
