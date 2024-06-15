from bson import ObjectId

from authentication import authenticate_api
from entities.comment_schema import Comment
from common import format_docs
from entities.post_schema import Post
from enums.response_code import ResponseCode
from enums.response_message import ResponseMessage
from models.response import SuccessResponse, Response, ErrorResponse
from validate_input.validate_inputs import validate_inputs
from service.connection import connect_mongo_post

collection_name =connect_mongo_post()

def add_post(request):
    try:
        response = authenticate_api(request=request, api_no=1)
        post = validate_inputs(schema=Post(), body=request.json)
        print(post)
        post['user_id'] = response['id']
        collection_name.insert_one(post)
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()

def get_user_post(request):
    try:
        response = authenticate_api(request=request, api_no=1)
        user_id = response['id']
        documents = collection_name.find({'user_id':user_id})
        response = {
            "state":True,
            "data":format_docs(documents)
        }
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()

def get_user_eligible_post(request):
    try:
        response = authenticate_api(request=request, api_no=1)
        user_id = response['id']
        documents = collection_name.find({'user_id':user_id,'eligibility':True})
        response = {
            "state":True,
            "data":format_docs(documents)
        }
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()

def add_comment(request , post_id):
    try:
        response = authenticate_api(request=request, api_no=1)
        comment = validate_inputs(schema=Comment(), body=request.json)
        comment['user_id'] = response['id']
        post = collection_name.find_one({'_id':ObjectId(post_id)})
        comments = post['comments']
        comments_count = post['comments_count']
        last_mint_count = post['last_mint_count']
        comments.append(comment)
        comments_count+=1
        if comments_count - last_mint_count >=10:
            post['eligibility'] = True
        post['comments_count'] = comments_count
        post['last_mint_count'] = last_mint_count
        post['comments'] = comments
        collection_name.update_one({'_id':ObjectId(post_id)},{'$set':post})
        return response
    except Exception as e:
        print(str(e))
        return (e if isinstance(e, Response) else ErrorResponse(ResponseCode.DB_QUERY_ERROR,
                                                                ResponseMessage.DB_QUERY_ERROR + str(e))).generate()

def get_post_comments(post_id):
    post = collection_name.find_one({'_id': ObjectId(post_id)})
    collection_name.update_one({'_id': ObjectId(post_id)},{'$set':{'eligibility':False}})
    comments = post['comments']
    return comments
