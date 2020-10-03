from flask import request, jsonify
from db.model import Client
from marshmallow import validate
from flask.views import MethodView
from helpers.data_manager import DataManager
from helpers.encrypt_pass import EncryptPass
from validators.client import ClientRegistration

data_m = DataManager()
encrypt = EncryptPass()
client_schema = ClientRegistration()

class Signin(MethodView):

    def post(self):
        try:
            client_signin = request.get_json()
            errors = client_schema.validate(client_signin)
            if errors:
                return jsonify({'error':errors}), 400
            # Falta realizar consulta del correo ingresado para verificar que el usuario no este registrado con el fin
            # de comunicar con mayor claridad el error ocasionado, de lo contrario el error solo sera generado en db
            new_client = Client(
                name_c = client_signin['name'],
                lastname_c = client_signin['last_Name'],
                email = client_signin['email'],
                password = client_signin['password'], # Falta encriptar la contrasena
                favorite_one = client_signin['favorite_one'],
                favorite_two = client_signin['favorite_two'],
                favorite_three = client_signin['favorite_three']
            )
            status = data_m.add(new_client)
            if status == 'ok':
                return jsonify({'status':'ok'}), 200
            elif status == 'error':
                return jsonify({'status':'error'}), 400
            else:
                return jsonify({'status':status}), 400
        except:
            return jsonify({'state':'error'}), 400
