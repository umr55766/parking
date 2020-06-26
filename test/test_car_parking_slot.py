import unittest

from src.Car import Car
from src.CarParkingSlot import CarParkingSlot


class CarParkingSlotTest(unittest.TestCase):
    def test_park_vehicle(self):
        # Given
        car = Car("KA-01-HH-2701", "Red")
        parking_slot = CarParkingSlot(10)

        # When
        parking_slot.park_vehicle(car)

        # Then
        self.assertEqual(parking_slot.get_parked_vehicle(), car)
