import unittest

from src.CarParkingSlot import CarParkingSlot
from src.Parking import Parking
from src.ParkingManager import ParkingManager


class ParkingTest(unittest.TestCase):
    def test_parking_slots(self):
        parking = Parking(10)

        self.assertEqual(len(parking._slots), 10)
        for slot in parking._slots:
            self.assertTrue(isinstance(slot, CarParkingSlot))

    def test_manager(self):
        self.assertTrue(isinstance(Parking(1).get_manager(), ParkingManager))