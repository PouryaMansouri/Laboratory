from abc import ABC, abstractmethod
import pickle
from typing import Type

import inspect
from core.models import BaseModel
import os

from user.models import Patient, BaseUser


class BaseManager(ABC):
    @abstractmethod
    def create(self, m: BaseModel):
        pass
    #
    # @abstractmethod
    # def save(self):
    #     pass


class FileManager(BaseManager):
    count: int = 1
    name_path: str
    list: list = []

    def __init__(self) -> None:
        super().__init__()
        # self.name_path = self.__class__.__name__.capitalize() + ".pkl"
        self.name_path = BaseModel.__name__.capitalize() + ".pkl"
        if os.path.exists(self.name_path):
            if os.stat(self.name_path).st_size:
                pickle_in = open(self.name_path, "rb")
                self.__class__.list = pickle.load(pickle_in)
                self.__class__.count = self.__class__.list[-1].id + 1
        else:
            open(self.name_path, "wb").close()
        self.id = self.__class__.count
        # self.__class__.count += 1

    def create(self, base_model: Type[BaseUser]):
        model = base_model()
        print(dir(model))
        print(dir(base_model))
        for _ in inspect.getmembers(model):
            if not _[0].startswith('_'):
                print(_)
        self.__class__.count += 1


fm = FileManager()
fm.create(BaseModel)
