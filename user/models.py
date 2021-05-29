from abc import ABC, abstractmethod
import pickle
from core.models import BaseModel
import os


class BaseUser(BaseModel, ABC):
    count: int = 1
    name_path: str
    list: list = []
    first_name: str
    last_name: str
    phone: str

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.phone = ""
        self.name_path = self.__class__.__name__.capitalize() + ".pkl"

        if os.path.exists(self.name_path):
            if os.stat(self.name_path).st_size:
                pickle_in = open(self.name_path, "rb")
                self.__class__.list = pickle.load(pickle_in)
                self.__class__.count = self.__class__.list[-1].id + 1
        else:
            open(self.name_path, "wb").close()
        self.id = self.__class__.count
        self.__class__.count += 1

    @abstractmethod
    def create(self):
        pass

    def save(self):
        self.__class__.list.append(self)
        with open(self.name_path, "wb") as f:
            pickle.dump(self.__class__.list, f)

    def read_all(self):
        with open(self.name_path, "rb") as f:
            unpickle = pickle.load(f)
        for _ in unpickle:
            print(_)


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

    def __repr__(self):
        return f"{self.id}.{self.first_name} {self.last_name}\nphone: {self.phone}"


#
#
# class Employee(BaseUser):
#     def __init__(self):
#         super().__init__()

if __name__ == '__main__':
    p = Patient()
    print(p.id)
    # p.create()
    # p.save()
    p.read_all()
