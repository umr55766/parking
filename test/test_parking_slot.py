import unittest

from src.ParkingSlot import ParkingSlot
from src.Vehicle import Vehicle


class ParkingSlotTest(unittest.TestCase):
    def test_park_vehicle(self):
        # Given
        vehicle = Vehicle("KA-01-HH-2701", "Red")
        parking_slot = ParkingSlot(10)

        # When
        parking_slot.park_vehicle(vehicle)

        # Then
        self.assertEqual(parking_slot.get_parked_vehicle(), vehicle)

    def test_unpark_vehicle(self):
        # Given
        vehicle = Vehicle("KA-01-HH-2701", "Red")
        parking_slot = ParkingSlot(10)
        parking_slot.park_vehicle(vehicle)

        # When
        parking_slot.unpark_vehicle()

        # Then
        self.assertEqual(parking_slot.get_parked_vehicle(), None)
