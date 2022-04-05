import os
import sys

from interact_package.token_setup import setup
from dotenv import load_dotenv, find_dotenv

from fyers_api import fyersModel
from fyers_api import accessToken

from interact_package.constants import *

load_dotenv(find_dotenv())

def read_file():
    with open("tokenf.txt", "r") as f:
        token = f.read()
    return token

client_id = os.getenv('client_id')

def profile():
    
    FYERS_ACCESS_TOKEN = setup()
    if FYERS_ACCESS_TOKEN != "" :   
        fyers = generate_fyers_model_object(FYERS_ACCESS_TOKEN)
        access_response = fyers.get_profile()
        if access_response.get('code') in error_access_response:
            setup()
            fyers = generate_fyers_model_object(FYERS_ACCESS_TOKEN)
            access_response = fyers.get_profile()
            print(access_response)
        else:
            print(access_response)
    


def generate_fyers_model_object(token):
    try:
        fyers = fyersModel.FyersModel(client_id=client_id, token=token, log_path=os.getcwd())
    except Exception as exception:
        print(exception)
    return fyers
