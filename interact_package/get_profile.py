import os
import sys

from interact_package.token_setup import setup
from dotenv import load_dotenv, find_dotenv

from fyers_api import fyersModel
from fyers_api import accessToken

load_dotenv(find_dotenv())

def read_file():
    with open("tokenf.txt", "r") as f:
        token = f.read()
    return token

client_id = os.getenv('client_id')

def profile():
    try:
            token = read_file()
    except FileNotFoundError:
        print("Getting the access token!")
        setup()
        sys.exit()
    fyers = fyersModel.FyersModel(client_id=client_id, token=token, log_path=os.getcwd())
    print(fyers.get_profile())
    
