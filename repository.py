import env

input = {
    "age":0,
    "gender":0,
    "tenure" :0,
    "friend_count":0,
    "likes":0,
    "supportive_tokens":0,
    "earned_tokens":0,
    "profession":0
}

registration_body ={
    "project_code":env.PROJECT_CODE,
    "email": "pulinitilanka_blockx@gmail.com",
    "password": "123456789",
    "email_confirmed": True,
    "admin_confirmed": True,
    "available_status" :"pending",
    "api_list" : [1],
    "type":"user",
    "data":"",
    "contact_no":"0776756786",
    "age":14,
    "gender":'male',
    "tenure" :266.0,
    "friend_count":3089,
    "likes":4201,
    "supportive_tokens":4761,
    "earned_tokens":4079,
    "profession":'Student',
    "profile_name":"subhath",
    "profile_picture":""
}

features = {
    "gender":{'male': 0, 'female': 1},
    "profession":{'Student': 0, 'Customer Service': 1, 'Fashion': 2, 'Proffesor': 3,
                  'Environmental Science': 4, 'Sports Management': 5, 'Public Relations': 6,
                  'Marketing': 7, 'Human Resources': 8, 'Social Work': 9, 'Manufacturing': 10,
                  'Event Planning': 11, 'Architecture': 12, 'Pharmaceuticals': 13, 'Insurance': 14, 'Energy': 15,
                  'Consulting': 16, 'Nonprofit Organizations': 17, 'Finance': 18, 'Culinary Arts': 19,
                  'Interior Design': 20, 'Transportation and Logistics': 21, 'Engineering': 22, 'Teacher': 23,
                  'Aerospace': 24, 'Banking': 25, 'Software Development': 26, 'Sales': 27, 'Telecommunications': 28, 'Real Estate': 29, 'Design': 30, 'Public Administration': 31, 'Photography': 32,
                  'Automotive': 33, 'Hospitality': 34, 'Research and Development': 35, 'Education': 36, 'Construction': 37,
                  'Fitness and Wellness': 38, 'Retail': 39, 'Agriculture': 40, 'Government': 41, 'Information Technology': 42, 'Project Management': 43,
                  'Entertainment and Media': 44, 'Journalism': 45, 'Cybersecurity': 46, 'Biotechnology': 47, 'Accountant': 48,
                  'Healthcare': 49, 'Data Analysis': 50, 'Psychology': 51, 'Legal': 52 ,'Nan':53}
}