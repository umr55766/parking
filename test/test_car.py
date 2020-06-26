import unittest

from src.Car import Car
from src.Vehicle import Vehicle


class CarTest(unittest.TestCase):
    def test_car(self):
        self.assertTrue(isinstance(Car(), Vehicle))
