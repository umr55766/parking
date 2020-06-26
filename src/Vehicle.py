from abc import ABC, abstractmethod


class Vehicle(ABC):
    def set_driver(self, driver):
        self._driver = driver

    def get_driver(self):
        return self._driver
