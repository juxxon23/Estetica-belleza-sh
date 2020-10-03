from marshmallow import Schema, fields, validate, validates, ValidationError

class ClientRegistration(Schema):
    name = fields.Str(required= True, validate= validate.Length(min= 3, max= 20))
    last_name = fields.Str(required= True, validate= validate.Length(min= 3, max= 20))
    email = fields.Str(required= True, validate= validate.Length(min= 13, max= 100))
    password = fields.Str(required= True, validate= validate.Length(min=8, max=20))


class ClientLogin(Schema):
    email = fields.Str(required= True, validate= validate.Length(min= 13, max= 100))
    password = fields.Str(required= True, validate= validate.Length(min=8, max=20))