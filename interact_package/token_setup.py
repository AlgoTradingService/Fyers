from dotenv import load_dotenv, find_dotenv

import os
import sys
from urllib.parse import urlparse, parse_qs
import requests



from fyers_api import fyersModel
from fyers_api import accessToken
from interact_package.constants import *


load_dotenv(find_dotenv())
username = os.getenv('username')
password = os.getenv('password')
pin = os.getenv('pin')
client_id = os.getenv('client_id')
secret_key = os.getenv('secret_key')
redirect_uri = os.getenv('redirect_uri')

app_id = client_id[:-4]  # "L9NY****W" (don't change this app_id variable)

FYERS_ACCESS_TOKEN = ""

def write_file(token):
    with open("tokenf.txt", "w") as f:
        f.write(token)


def setup():
    global FYERS_ACCESS_TOKEN
    session = accessToken.SessionModel(
        client_id=client_id,
        secret_key=secret_key,
        redirect_uri=redirect_uri,
        response_type="code",
        grant_type="authorization_code",
    )

    s = requests.Session()

    data1 = f'{{"fy_id":"{username}","password":"{password}","app_id":"2","imei":"","recaptcha_token":""}}'
    r1 = s.post("https://api.fyers.in/vagator/v1/login", data=data1)

    # assert r1.status_code == 200, f"Error in r1:\n {r1.json()}"
    if not r1.status_code in success_response_codes:
        return response_code_values.get(r1.status_code)


    request_key = r1.json()["request_key"]

    data2 = f'{{"request_key":"{request_key}","identity_type":"pin","identifier":"{pin}","recaptcha_token":""}}'
    r2 = s.post("https://api.fyers.in/vagator/v1/verify_pin", data=data2)

    assert r2.status_code == 200, f"Error in r2:\n {r2.json()}"

    headers = {"authorization": f"Bearer {r2.json()['data']['access_token']}", "content-type": "application/json; charset=UTF-8"}
    data3 = f'{{"fyers_id":"{username}","app_id":"{app_id}","redirect_uri":"{redirect_uri}","appType":"100","code_challenge":"","state":"abcdefg","scope":"","nonce":"","response_type":"code","create_cookie":true}}'
    r3 = s.post("https://api.fyers.in/api/v2/token", headers=headers, data=data3)

    assert r3.status_code == 308, f"Error in r3:\n {r3.json()}"
    try:
        if FYERS_ACCESS_TOKEN == "" :
            parsed = urlparse(r3.json()["Url"])
            auth_code = parse_qs(parsed.query)["auth_code"][0]
            session.set_token(auth_code)
            response = session.generate_token()
            FYERS_ACCESS_TOKEN = response["access_token"]
    except Exception as exception:
        FYERS_ACCESS_TOKEN = ""
        print(exception)
        
    return FYERS_ACCESS_TOKEN