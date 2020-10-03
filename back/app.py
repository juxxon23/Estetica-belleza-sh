from flask import Flask
from flask_cors import CORS
from db.model import db
from routes import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/EsteticaTest"
CORS(app, supports_credentials=True)
db.init_app(app)

# Client routes
app.add_url_rule(client['signin'], view_func= client['view_func_signin'])
app.add_url_rule(client['login'], view_func=client['view_func_login'])

# Appointment routes
app.add_url_rule(appointment['appointment'], view_func=appointment['view_func_appointment'])