import time
from bson import ObjectId
from blockchian_plugin import do_transaction, store_transaction, get_chain
from common import format_docs
from service.connection import connect_mongo_validation_requests , connect_mongo_requests

collection_name_validation = connect_mongo_validation_requests()
collection_name_request = connect_mongo_requests()

def add_validation(private_key , reciever_public_key , amount , transferer_public_key , request_id):
    response = do_transaction(private_key , reciever_public_key , amount , transferer_public_key)
    try:
        validation_request = {
            "block": response['block'],
            "request_id":request_id,
            "time_stamp":time.time(),
            "validated_keys":[]
        }
        collection_name_validation.insert_one(validation_request)
        return response
    except:
        return response

def get_validates(request):
    body = request.json
    public_key = body['public_key']
    user_validations = []
    validations = collection_name_validation.find()
    for validation in validations:
        request = collection_name_request.find_one({'_id':ObjectId(validation['request_id'])})
        if public_key in request['public_keys'] and not public_key in validation['validated_keys']:
            user_validations.append(validation)
    return format_docs(user_validations)

def validate_transaction(request):
    body = request.json
    print(body)
    public_key = body['public_key']
    validation_id = body['validation_id']
    validation = collection_name_validation.find_one({'_id':ObjectId(validation_id)})
    print(validation)
    validated_keys = validation['validated_keys']
    print(validated_keys)
    validated_keys.append(public_key)
    collection_name_validation.update_one({'_id':ObjectId(validation_id)},{'$set':{'validated_keys':validated_keys}})
    return {
        "state":True
    }

def check_whether_validated_or_rejected(time_limit):
    validations = collection_name_validation.find()
    for validation in validations:
        request = collection_name_request.find_one({'_id':ObjectId(validation['request_id'])})
        if len(validation['validated_keys'])>=len(request['public_keys']) / 2:
            #store transaction
            store_transaction(validation['block'])
            collection_name_validation.delete_one({'_id':validation['_id']})
        elif time.time() > validation['time_stamp'] + time_limit:
            collection_name_validation.delete_one({'_id':validation['_id']})

def get_chain_blocks(request):
    body = request.json
    public_key = body['public_key']
    response = get_chain(public_key)
    print(response)
    return response





