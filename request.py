import datetime
import threading
import time
from collections import defaultdict

from bson import ObjectId

lock = threading.Lock()
from blockchian_plugin import select_nodes
from cache import set_id, get_cache, add_cache, check_cache, set_start, set_finished, check_operation
from check_post_content import check_image
from common import format_docs, format_doc
from posts import get_post_comments
from prediction import detect_comments
from user import return_profile_data, return_user_data, check_blockchain_registration
from user_account_score import user_acount_score_calculate
from service.connection import connect_mongo_requests , connect_mongo_post


collection_name = connect_mongo_requests()
collection_name_post = connect_mongo_post()
def get_predictions(user_ids):
    scores = {}
    for user_id in user_ids:
        score = user_acount_score_calculate(acount_data=return_user_data(user_id))
        scores[user_id] = score
    return scores

def token_request_operation(data):
    time.sleep(5)
    print("start_thread_ops")
    user_public_key = data['user_public_key']
    request = data['request']
    body = data['body']
    id = data['id']
    set_start(id)
    res = select_nodes(user_public_key)
    print(res)
    public_keys = res['public_keys']
    profile_data = return_profile_data(request)
    print(profile_data)
    user_score = user_acount_score_calculate(acount_data=profile_data)
    print(user_score)
    post = check_image()
    comments = get_post_comments(post_id=body['post_id'])
    detected_comments = detect_comments(comments)
    print(detected_comments)
    user_ids = list(map(lambda comment: comment['user_id'], detected_comments))
    print(user_ids)
    user_ids = list(set(user_ids))
    scores = get_predictions(user_ids)
    print(scores)
    grouped_user_ids = defaultdict(list)
    for item in detected_comments:
        grouped_user_ids[item['class']].append(item['user_id'])
    grouped_user_ids = dict(grouped_user_ids)
    print(grouped_user_ids)
    comment_level = {}
    for item in grouped_user_ids:
        user_ids = grouped_user_ids[item]
        total_score = sum(map(lambda x: scores[x], user_ids))
        comment_level[item] = {
            'total_score': total_score,
            'average': total_score / len(user_ids),
            'comments': len(user_ids)
        }
    print(comment_level)
    guidance = {
        "user_score": user_score,
        "post_grade": post[0],
        "comment_level": comment_level,
        "post_id": body['post_id'],
        "public_keys": public_keys,
        "user_public_key": user_public_key,
        "expire_time": time.time() + 3600 * 24 * 7,
        "time_stamp": datetime.datetime.today()
    }
    collection_name.insert_one(guidance)
    print(guidance)
    response_document =  {
        "state": True,
        "guidance": format_doc(guidance)
    }
    set_finished(id)
    add_cache(response_document, id)
    collection_name_post.update_one({'_id':ObjectId(body['post_id'])},{'$set':{'eligibility':False}})
    return

def get_id():
    id = set_id()
    return {
        'state':True,
        'id':id
    }
def request_tokens(request):
    user_public_key = check_blockchain_registration(request)
    body = request.json
    id = body['id']
    if not check_cache(id):
        data = {
            'id':id,
            'user_public_key':user_public_key,
            'request':request,
            'body':body
        }
        token_request_operation(data)
        return {
            "state": True,
            "id": id
        }
    else:
        return {}

def get_request_response(id):
    return get_cache(id)
def get_requests(request):
    body = request.json
    public_key = body['public_key']
    user_requests = []
    requests = list(collection_name.find())
    for request in requests:
        if public_key in request['public_keys']:
            del request['public_keys']
            user_requests.append(request)
    return format_docs(user_requests)

def check_request_time():
    token_requests = collection_name.find()
    for request in token_requests:
        if time.time() > request['expire_time']:
            collection_name.delete_one({'_id':request['_id']})

