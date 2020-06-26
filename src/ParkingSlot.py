from abc import ABC, abstractmethod


class ParkingSlot(ABC):
    def __init__(self, serial_number):
        self._parked_vehicle = None
        self._serial_number = serial_number

    def park_vehicle(self, vehicle):
        self._parked_vehicle = vehicle

    def get_parked_vehicle(self):
        return self._parked_vehicle
