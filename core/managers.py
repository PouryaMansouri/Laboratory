from abc import ABC, abstractmethod

from core.models import BaseModel


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
