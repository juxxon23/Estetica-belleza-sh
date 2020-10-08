from marshmallow import Schema, fields, validate, validates, ValidationError

class AppointmentVal(Schema):
    id_c = fields.Str(required= True)
    id_e = fields.Str(required= True)
    id_s = fields.Str(required= True)
    date = fields.DateTime(required=True)