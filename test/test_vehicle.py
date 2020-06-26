import unittest

from src.Vehicle import Vehicle


class VehicleTest(unittest.TestCase):
    def test_valid_registration_number(self):
        self.assertTrue(isinstance(Vehicle("KA-01-HH-2701", "Red"), Vehicle))

    def test_invalid_registration_number(self):
        with self.assertRaises(ValueError):
            Vehicle("invalid-number", "Color")