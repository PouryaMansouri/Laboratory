from abc import ABC, abstractmethod
import pickle
from core.models import BaseModel
import os


class BaseUser(BaseModel, ABC):
    __count: int = 1
    __name_path: str
    __list: list = []

    def __init__(self):
        self.id = self.__class__.__count
        self.__class__.__count += 1
        self.__name_path = self.__class__.__name__.capitalize() + ".pkl"

        if os.path.exists(self.__name_path):
            if os.stat(self.__name_path).st_size:
                pickle_in = open(self.__name_path, "rb")
                self.__class__.__list = pickle.load(pickle_in)
                print("asdasd")
        else:
            open(self.__name_path, "wb").close()

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def save(self):
        pass


# class Doctor(BaseUser):
#     def __init__(self):
#         super().__init__()


class Patient(BaseUser):
    def __init__(self):
        super().__init__()

    def create(self):
        self.first_name = input("first_name: ")
        self.last_name = input("last_name: ")
        self.phone = input("phone: ")

    def save(self):
        pass


#
#
# class Employee(BaseUser):
#     def __init__(self):
#         super().__init__()


p = Patient()
print(p.id)
