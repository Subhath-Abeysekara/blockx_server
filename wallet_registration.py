from authentication import authenticate_api
from blockchian_plugin import register_user
from check_email_availability import check_email_availability
from service.connection import connect_mongo_user
collection_name = connect_mongo_user()

def register(request):
    email = request.json['email']
    email_data = check_email_availability(email=email)
    if email_data['state']:
        user_id = email_data['user_id']
        document = collection_name.find_one({'auth_id': user_id})
        data =  register_user()
        print(document)
        if data['state']:
            public_key = data['public_key']
            print(public_key)
            document['public_key'] = public_key
            print(document)
            collection_name.update_one({'_id': document['_id']},{'$set': document})
            return data
    return {
        'state':False,
        'error':'Not a social media user'
    }