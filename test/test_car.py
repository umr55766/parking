import unittest

from src.Car import Car
from src.Driver import Driver
from src.Vehicle import Vehicle


class CarTest(unittest.TestCase):
    def test_car(self):
        car = Car("KA-01-HH-2701", "Red")
        self.assertTrue(isinstance(car, Vehicle))
        self.assertEqual(car._registration_number, "KA-01-HH-2701")
        self.assertEqual(car._color, "Red")

    def test_car_driver(self):
        # Given
        car = Car("KA-01-HH-2701", "Red")
        driver = Driver()

        # When
        car.set_driver(driver)

        # Then
        self.assertEqual(car.get_driver(), driver)
