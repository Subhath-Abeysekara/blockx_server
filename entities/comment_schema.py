from marshmallow import Schema, fields, validate
from datetime import date, datetime

class Comment(Schema):
    date = fields.Str(dump_default=str(date.today()))
    time = fields.Str(dump_default=datetime.now().strftime('%H:%M'))
    comment = fields.Str(required=True)
    user_id = fields.Str(dump_default="")
