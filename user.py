import requests
import env
import repository
from authentication import authenticate_api
from common import format_docs, format_doc
from entities.user_schema import User
from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
from models.response import SuccessResponse, Response, ErrorResponse
from service.connection import connect_mongo_user
from validate_input.validate_inputs import validate_inputs

collection_name = connect_mongo_user()

def add_user(body):
    try:
        print(body)
        url = env.AUTHORIZATION_URL + "/addUser"
        validate_res = requests.post(url=url, json=body)
        print(validate_res.json())
        if validate_res.json()['data']['state']:
            user = validate_inputs(schema=User(), body=body)
            user['auth_id'] = validate_res.json()['data']['id']
            print(user)
            collection_name.insert_one(user)
        response = validate_res.json()['data']
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()


def return_profile_data(request):
    response = authenticate_api(request=request, api_no=1)
    user_id = response['id']
    document = collection_name.find_one({'auth_id': user_id})
    return format_doc(document)

def check_blockchain_registration(request):
    response = authenticate_api(request=request, api_no=1)
    user_id = response['id']
    document = collection_name.find_one({'auth_id': user_id})
    try:
        return document['public_key']
    except:
        raise Exception(
            ErrorResponse(ResponseCode.MISSING_TOKEN, ResponseMessage.MISSING_TOKEN + str("Not registered to chain")))

def return_user_data(user_id):
    document = collection_name.find_one({'auth_id': user_id})
    return format_doc(document)

def get_profile_data(request):
    try:
        response = {
            "state": True,
            "data":return_profile_data(request=request)
        }
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()

# add_user(repository.registration_body)
# schema = User()
# user = validate_inputs(schema=schema , body=repository.registration_body)
# print(user)