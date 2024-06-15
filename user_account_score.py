from prediction import predict_user_score
from repository import features ,input


def user_acount_score_calculate(acount_data):
    datapoint = []
    keys = input.keys()
    keys_list = list(keys)
    print(keys_list)
    keys_feature = features.keys()
    keys_list_feature = list(keys_feature)
    print(keys_list_feature)
    for key in keys_list:
        print(key)
        try:
            if not key in keys_list_feature:
                print(acount_data[key])
                datapoint.append(int(acount_data[key]))
            else:
                print(features[key][acount_data[key]])
                datapoint.append(features[key][acount_data[key]])
        except:
            try:
                print(features[key]['nan'])
                datapoint.append(features[key]['nan'])
            except:
                return False
    prediction = predict_user_score(datapoint)
    return prediction

data = {
    "age":14,
    "gender":'male',
    "tenure" :266.0,
    "friend_count":3089,
    "likes":4201,
    "supportive_tokens":4761,
    "earned_tokens":4079,
    "profession":'Student'
}

# print(user_acount_score_calculate(acount_data=data))