import unittest

from src.Car import Car
from src.Driver import Driver
from src.Vehicle import Vehicle


class CarTest(unittest.TestCase):
    def test_car(self):
        self.assertTrue(isinstance(Car(), Vehicle))

    def test_car_driver(self):
        # Given
        car = Car()
        driver = Driver()

        # When
        car.set_driver(driver)

        # Then
        self.assertEqual(car.get_driver(), driver)
