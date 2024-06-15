import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate("meetingdetecting-firebase-adminsdk-i1m1b-578553aeaa.json")
firebase_admin.initialize_app(cred)
count = 0
def upload_image_to_firebase(image_file):
    global count
    bucket = storage.bucket('meetingdetecting.appspot.com')
    file_name = "eco_image_"+str(count)
    count+=1
    destination_blob_name = f'images_eco_print/{file_name}'
    blob = bucket.blob(destination_blob_name)
    with open(image_file, 'rb') as f:
        blob.upload_from_file(f,content_type='image/jpeg')
    return file_name

def get_sign_url_firebase(file_name):
    bucket = storage.bucket('meetingdetecting.appspot.com')
    destination_blob_name = f'images_eco_print/{file_name}'
    blob = bucket.blob(destination_blob_name)
    expiration_date = 604000  # Set the expiration time (e.g., 1 hour)
    signed_url = blob.generate_signed_url(version='v4',expiration=expiration_date)
    return signed_url

def download_from_firebase():
    # Get a reference to the Firebase Storage bucket
    bucket = storage.bucket('meetingdetecting.appspot.com')
    destination_blob_name = f'blockX/comment_level_predict_model.h5'
    blob = bucket.blob(destination_blob_name)
    blob.download_to_filename("comment_level_predict_model.h5")
    return