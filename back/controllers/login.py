from flask.views import MethodView
from flask import request, jsonify
from marshmallow import validate
from validators.client_val import ClientLogin
from db.model import Client
from config import KEY_TOKEN_AUTH
import bcrypt
import jwt
import datetime

client_schema = ClientLogin()

class login(MethodView):

    def post(self):
        client_login = request.get_json()
        errors = client_schema.validate(client_login)
        if errors:
            return jsonify({'error':errors}), 400
        client_db = Client.query.filter_by(id_c=client_login['document']).first()
        if client_db != None:
            if bcrypt.checkpw(client_login['password'].encode('utf-8'), client_db.password.encode('utf-8')):
                encoded_jwt = jwt.encode({'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=300), 'nombre':client_db.name_c}, KEY_TOKEN_AUTH, algorithm='HS256')
                return jsonify({'status':'ok', 'token':encoded_jwt}), 200
            else:
                return jsonify({'status':'password'}), 400
        else:
            return jsonify({'status':'document'}), 400

