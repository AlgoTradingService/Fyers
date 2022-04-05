from time import time
from interact_package import get_profile
import sys

import threading
exit = ""

def excecute():
    
    if exit == "EXIT":
        sys.exit(2)
    else:
        print(get_profile.profile())
        timer = threading.Timer(5, excecute)


def take_user_input():
    user_input = input("Do you wanna continue ?")
    global exit
    exit = user_input
    timer2 = threading.Timer(1 , take_user_input)


excecute()

take_user_input()

