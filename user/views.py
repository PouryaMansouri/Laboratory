from tests.models import CoronaTest
from user.models import Patient
from typing import List


def login() -> bool:
    global LOGIN
    url = ""
    print("login kardi")
    username = input()
    password = input()
    # TODO: manager --> read unpickle
    # unpickle = list()
    # for _ in unpickle:
    #     if _.username == username:
    #         if _.password == password:
    #             LOGIN = True
    #             print("login sdfad")
    #             break
    # else:
    #     print("no login ")


def register() -> Patient:
    print("register")


def logout():
    pass


def corona_test_view() -> CoronaTest:
    # TODO: check login or register
    # TODO: test_time
    # TODO: result_time ( 3day later)
    # TODO: result = ""
    # TODO: description = ""
    # TODO: test = CoronaTest(test_time, ...)
    # TODO : return test
    pass


def cbc_test_view():
    pass
