import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
import pandas as pd

from firebase_model_download import download_from_firebase
from presprocess_comment import preprocess_sentence


def predict_user_score(datapoint):
    numpy_data = np.array(datapoint)
    print(numpy_data)
    load_model = joblib.load('user_score_predict_model_final.h5')
    predictions = load_model.predict(numpy_data.reshape(1, -1))
    return predictions[0]

def detect_post_content(img_array):
    label = {'Very Bad':4, 'Bad':3, 'Neutral':2, 'Good':1, 'Very Good':0}
    load_model = joblib.load('post_level_predict_model_final.h5')
    predictions = load_model.predict(img_array)
    post_prediction = [key for key, value in label.items() if value == predictions]
    print(post_prediction)
    return post_prediction

def detect_comment_level(comment_obj):
    print(comment_obj)
    comment = comment_obj['comment']
    user_id = comment_obj['user_id']
    label = {'Very Bad':4, 'Bad':3, 'Neutral':2, 'Good':1, 'Very Good':0}
    comment = preprocess_sentence(sentence=comment)
    load_model = joblib.load('comment_level_predict_model.h5')
    tfidf_vectorizer = TfidfVectorizer(max_features=20)
    x_train = pd.read_csv("x_train.csv")
    x_train = x_train.dropna()
    missing_values = x_train.isna().sum()
    print(missing_values)
    X_test_ = [comment]
    X_train_tfidf = tfidf_vectorizer.fit_transform(list(x_train['content']))
    X_test_tfidf = tfidf_vectorizer.transform(X_test_)
    print(X_test_tfidf)
    comment_pred = load_model.predict(X_test_tfidf)
    comment_pred = [key for key, value in label.items() if value == comment_pred]
    print(comment_pred[0])
    return {
        'class':comment_pred[0],
        'user_id':user_id
    }

def detect_comments(comments):
    return list(map(lambda comment: detect_comment_level(comment_obj=comment), comments))
# sentence = "hi This is an example sentence with some stop words."
# print(detect_comment_level(sentence))
# datapoint = [5999,258,770,14,2,5347,1,0,1,24,236,0,3319,1,5,201]
# datapoint = [14,0,266.0,3005,2378,6304,3336,0]
# print(predict_user_score(datapoint))
