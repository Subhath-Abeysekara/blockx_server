from marshmallow import Schema, fields, validate


class User(Schema):
    age = fields.Int(required=True)
    profile_name = fields.Str(required=True)
    profession = fields.Str(required=True)
    auth_id = fields.Str(dump_default="")
    profile_picture = fields.Str(dump_default="")
    gender = fields.Str(required=True)
    earned_tokens = fields.Int(required=True)
    supportive_tokens = fields.Int(required=True)
    likes = fields.Int(required=True)
    tenure = fields.Int(required=True)
    friend_count = fields.Int(required=True)
