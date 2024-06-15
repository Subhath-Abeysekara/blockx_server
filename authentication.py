import requests
import os
from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
import env
from models.response import ErrorResponse


def authenticate_api(request , api_no):
    try:
        token = request.headers.get('token')
        headers = {'project_code': env.PROJECT_CODE,
                   'token': token}
        print(headers)
        url = env.AUTHORIZATION_URL+"/userAuth/"+str(api_no)
        validate_res = requests.get(url=url , headers=headers)
        print(validate_res.json())
        if not validate_res.json()['data']['state']:
            raise Exception(
                ErrorResponse(ResponseCode.INVALID_AUTHENTICATION,
                              ResponseMessage.INVALID_AUTHENTICATION + str("error")))
        else:
            response = {
                "state": True,
                "id": validate_res.json()['data']['code']
            }
    except:
        raise Exception(
            ErrorResponse(ResponseCode.MISSING_TOKEN, ResponseMessage.MISSING_TOKEN + str("error")))
    return response

# event = {
#     "headers":{
#         "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFiZXlzZWthcmFzZHBAZ21haWwuY29tIiwicGFzc3dvcmQiOiIxMjM0NTY3ODkiLCJjb2RlIjoiNjYwYTMyODNlNWQwNDQxODU0YWVhMDQ1IiwiZXhwaXJlIjoxNzEyNDYwNTk4fQ.GmZe-lpFCSBzl_jkeNBJyLSx6uByEMOqM_lHgnFNhds"
#     }
# }
#
# authenticate_api(event , 1)