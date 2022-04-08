from time import time
from interact_package import get_profile
import sys, select


TIMEOUT = 5
import threading
exit = ""

def excecute():
    global exit
    if exit == "EXIT":
        sys.exit(2)
    else:
        print(get_profile.profile())
        timer = threading.Timer(10, excecute) # Executing this thread for every 10 seconds.
        timer.start()


def user_input():
    global exit
    while True:
        print("If you want to exit, type 'EXIT' and press Enter.")

        i, o, e = select.select([sys.stdin], [], [], 5)
        if i:
            ui = sys.stdin.readline().strip()
            if ui == 'EXIT':
                exit = ui
                sys.exit(4)

excecute()

user_input()

 




