from flask import Flask
from flask_cors import CORS
from routes import consultant, login, customer, equipment, line, bill

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
