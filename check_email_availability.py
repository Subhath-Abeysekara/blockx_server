import requests
import env


def check_email_availability(email):
    try:
        body = {'project_code': env.PROJECT_CODE,
                   'email': email}
        url = env.AUTHORIZATION_URL+"/email_availability"
        validate_res = requests.post(url=url , json=body)
        print(validate_res.json())
        return validate_res.json()['data']
    except Exception as e:
        print(str(e))
        return False

# email = "abeysekarasdp@gmail.com"
# check_email_availability(email)