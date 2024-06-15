from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
from models.response import ErrorResponse


def validate_inputs(schema , body):
    body = schema.dump(body)
    errors = schema.validate(body)
    if errors:
        raise Exception(
            ErrorResponse(ResponseCode.INVALID_INPUT_FORMAT, ResponseMessage.INVALID_INPUT_FORMAT + str(errors)))
    return body