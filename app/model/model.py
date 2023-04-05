# import required libraries and modules
from marshmallow import Schema, fields, validate

# define list of valid vields
VALID_CMD = ('filter', 'map', 'sort', 'limit', 'unique')


# creating schema according to required form
class RequestSchema(Schema):
    cmd = fields.Str(required=True, validate=validate.OneOf(VALID_CMD))
    value = fields.Str(required=True)



class BatchRequestSchema(Schema):
    queries = fields.Nested(RequestSchema, many=True)
    file_name = fields.Str(required=True)
