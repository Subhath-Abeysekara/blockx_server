import  json
import re
from entities.messages import get_massages
RESPONSE_HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*', # Required for CORS support to work
    'Access-Control-Allow-Credentials': True, # Required for cookies, authorization headers with HTTPS
}

class Response:
    def __init__(self, state, data, status_code = 400, code  = 10, response_message =''):
        print("data : ",data)
        print(code)
        print(str(response_message))
        pattern = r"<ResponseCode\.ORDER_UPDATE_ERROR: (\d+)>"
        match = re.search(pattern, str(response_message))
        number = 0
        message = "default"
        if match:
            number = int(match.group(1))
        print(number)
        pattern = r"<ResponseMessage\.PACKET_LIMIT_ERROR: '(.*?)'>"
        match = re.search(pattern, str(response_message))
        if match:
            message = match.group(1)
        print(message)

        if data == {}:
            data = {"message":get_massages()[message]}
        self.body = {
            'state': state,
            'data':data,
            'code': code,
            'message': response_message
        }
        self.status_code = status_code

    def generate(self):
        return {
            'statusCode': self.status_code,
            'headers': RESPONSE_HEADERS,
            'body': json.dumps(self.body)
        }

class SuccessResponse(Response):
    def __init__(self, data):
        super().__init__(True,data,200,0,'success')

class SuccessMessageResponse(Response):
    def __init__(self, message):
        super().__init__(True,{'info':message},200,0,'success')


class ErrorResponse(Response,Exception):
    def __init__(self, response_code,response_message):
        super().__init__(False,{},400,response_code,response_message)


