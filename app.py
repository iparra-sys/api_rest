from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB
from models import db
from resources.item_resource import ItemResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DB}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()  # crea las tablas en MySQL

# Registrar endpoints
api.add_resource(ItemResource, '/items', '/items/<int:item_id>')

if __name__ == "__main__":
    app.run(debug=True)
