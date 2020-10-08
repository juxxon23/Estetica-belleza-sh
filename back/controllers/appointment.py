from flask.views import MethodView
from flask import request, jsonify
from marshmallow import validate
from db.model import Appointment
from validators.appointment_val import AppointmentVal
from helpers.data_manager import DataManager

appointment_schema = AppointmentVal()
data_m = DataManager()

class appointment(MethodView):
    def post(self):
        appointment_data = request.get_json()
        errors = appointment_schema.validate(appointment_data)
        if errors:
            return jsonify({'error': errors}), 400
        try:
            appointment_new = AppointmentVal(
                id_client = appointment_data['id_c'],
                id_employee = appointment_data['id_e'],
                id_services = appointment_data['id_s'],
                date_a = appointment_data['date']
            )
            status = data_m.add(appointment_new)
            if status == 'ok':
                return jsonify({'status':'ok'}), 200
            elif status == 'error':
                return jsonify({'status':"error"}), 400
            else:
                return jsonify({'status':status}), 400
        except:
            return jsonify({'status':'error'}), 400

