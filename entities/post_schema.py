from marshmallow import Schema, fields, validate
from datetime import date, datetime

class Post(Schema):
    date = fields.Str(dump_default=str(date.today()))
    time = fields.Str(dump_default=datetime.now().strftime('%H:%M'))
    url = fields.Str(required=True)
    user_id = fields.Str(dump_default="")
    comments = fields.List(fields.Dict(), dump_default=[])
    comments_count = fields.Int(dump_default=0)
    last_mint_count = fields.Int(dump_default=0)
    eligibility = fields.Bool(dump_default=False)
