import re
from abc import ABC

from src.configs import Configs


class Vehicle(ABC):
    def __init__(self, registration_number, color):
        if not re.match(Configs.REGISTRATION_NUMBER_FORMAT, registration_number):
            raise ValueError("Invalid registration number")

        self._registration_number = registration_number
        self._color = color

    def set_driver(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver
