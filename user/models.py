from abc import ABC

from core.models import BaseModel


class BaseUser(BaseModel, ABC):
    pass


class Doctor(BaseUser):
    pass


class Patient(BaseUser):
    pass


class Personal(BaseUser):
    pass


