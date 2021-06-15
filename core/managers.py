from abc import ABC, abstractmethod
from typing import Type

from psycopg2 import connect
from psycopg2._psycopg import connection, cursor

import settings
from core.models import BaseModel
from user.models import BaseUser


class BaseManager(ABC):

    @abstractmethod
    def create(self, m: BaseModel) -> ...:
        pass

    @abstractmethod
    def read(self, id: int) -> BaseModel:
        pass

    @abstractmethod
    def update(self, id: int, m: BaseModel) -> None:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass


class FileManger(BaseManager):
    pass


class DBManager(BaseManager):
    DB_CONFIG: dict = getattr(settings, 'DB_CONFIG')

    def __init__(self, base_model: Type[BaseUser], tb_name=None) -> None:
        self.base_model = base_model
        self.tb_name = tb_name or base_model.__name__.lower()
        config_line = " ".join(map(lambda i: f"{i[0]}='{i[1]}", self.DB_CONFIG.items()))
        self.conn: connection = connect(config_line)

    def create(self, m: BaseUser) -> ...:
        data: dict = m.to_dict()

        def value_normalizer(value):
            if value is None:
                return 'NULL'
            if isinstance(value, dict):
                return str(Json(value))
            if isinstance(value, str):
                return f"'{value}'"
            return value

        keys = data.keys()
        values = map(value_normalizer, data.values())
        curs: cursor = self.conn.cursor()


