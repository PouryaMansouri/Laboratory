LOGIN = False
import pickle
from user.models import Patient
from typing import List


def login():
    global LOGIN
    URL = "user/Patient.pkl"
    if LOGIN == True:
        print('you have already logged in')
    else:
        firstname = input("please enter your username :")
        password = input("please enter your phone number :")
        with open(URL, 'rb') as f:
            unpickle = pickle.load(f)
        for i in unpickle:
            if i.first_name == firstname:
                if i.phone == password:
                    LOGIN = True
                    print(' logged in sucessfully')
                    break
        else:
            print('your username or password is incorrect')
