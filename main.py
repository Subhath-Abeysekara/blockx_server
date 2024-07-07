from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,request
from flask_cors import CORS , cross_origin

from blockchian_plugin import start_client, login_user, do_transaction
from check_post_content import check_image
from firebase_model_download import download_from_firebase
from posts import add_post, get_user_post, get_user_eligible_post, add_comment
from request import request_tokens, get_requests
from scheduler import scheduler_operation
from user import get_profile_data
from user_account_score import user_acount_score_calculate
from wallet_registration import register
from wallet_transaction import validate_transaction, get_validates, get_chain_blocks, add_validation

app = Flask(__name__)
CORS(app , resources={r"/":{"origins":"*"}})
try:
    download_from_firebase()
    print("model_downloaded")
except:
    print("download error")


scheduler = BackgroundScheduler()
scheduler.add_job(scheduler_operation, trigger='interval', seconds=43200)
scheduler.start()
@app.route("/")
def main():
    return "hello world"

@app.route("/home")
@cross_origin()
def home():
    return "First Page"

@app.route("/v1/prediction", methods=["POST"])
@cross_origin()
def image_upload_undefined():
    uploaded_file = request.files['image']
    body = request.form.to_dict(flat=False)
    print(body)
    if uploaded_file:
        uploaded_file.save('uploaded.png')
        try:
            response_post = check_image()
            response_score = user_acount_score_calculate(acount_data=body)
            return {
                "post":response_post,
                "score":response_score
            }
        except:
            return {
                "message": "Error",
                "state": False
            }

@app.route("/v1/request_token", methods=["POST"])
@cross_origin()
def request_():
    return request_tokens(request)

@app.route("/v1/post", methods=["POST"])
@cross_origin()
def add_post_():
    return add_post(request=request)

@app.route("/v1/user_profile", methods=["GET"])
@cross_origin()
def user_profile():
    return get_profile_data(request=request)

@app.route("/v1/user_posts", methods=["GET"])
@cross_origin()
def user_post():
    return get_user_post(request=request)

@app.route("/v1/user_eligible_posts", methods=["GET"])
@cross_origin()
def user_eligible_post():
    return get_user_eligible_post(request=request)

@app.route("/v1/comment/<post_id>", methods=["PUT"])
@cross_origin()
def comment(post_id):
    return add_comment(request=request , post_id=post_id)

######### PLUGIN #############

@app.route("/wallet/register", methods=["POST"])
@cross_origin()
def wallet_register():
    try:
        return register(request = request)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

@app.route("/wallet/login", methods=["POST"])
@cross_origin()
def wallet_login():
    try:
        private_key = request.json['private_key']
        return login_user(private_key)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }


@app.route("/wallet/get_requests", methods=["POST"])
@cross_origin()
def get_relavent_requests():
    try:
        return get_requests(request=request)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

@app.route("/wallet/transaction", methods=["POST"])
@cross_origin()
def wallet_transaction():
    try:
        data = request.json
        private_key = data['private_key']
        reciever_public_key = data['reciever_public_key']
        transferer_public_key = data['transferer_public_key']
        request_id = data['request_id']
        amount = data['amount']
        return add_validation(private_key , reciever_public_key , amount , transferer_public_key , request_id=request_id)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

@app.route("/wallet/get_chain", methods=["POST"])
@cross_origin()
def get_blockchain():
    try:
        return get_chain_blocks(request=request)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

@app.route("/wallet/get_validation_requests", methods=["POST"])
@cross_origin()
def get_blockchain():
    try:
        return get_validates(request=request)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

@app.route("/wallet/validate_request", methods=["POST"])
@cross_origin()
def get_blockchain():
    try:
        return validate_transaction(request)
    except Exception as e:
        return {
            'state':False,
            'error':str(e)
        }

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost',port=5000)
