from flask import Flask
#from flask_cors import CORS
from db.model import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/EsteticaTest"

CORS(app, supports_credentials=True)
db.init_app(app)