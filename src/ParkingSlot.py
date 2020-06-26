from abc import ABC, abstractmethod


class ParkingSlot(ABC):
    def __init__(self, serial_number):
        self._parked_vehicle = None
        self._serial_number = serial_number

    def get_serial_number(self):
        return self._serial_number

    def park(self, vehicle):
        self._parked_vehicle = vehicle

    def get_parked_vehicle(self):
        return self._parked_vehicle

    def unpark_vehicle(self):
        self._parked_vehicle = None
