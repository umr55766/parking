from src.CarParkingSlot import CarParkingSlot
from src.ParkingManager import ParkingManager
from src.TicketSystem import TicketSystem


class Parking:
    def __init__(self, slots):
        self._slots = [CarParkingSlot(_) for _ in range(1, slots + 1)]
        self._manager = ParkingManager(TicketSystem(), self._slots)

    def get_slot_by_serial_number(self, serial_number):
        for slot in self._slots:
            if slot.get_serial_number() == serial_number:
                return slot

    def unpark(self, slot):
        slot.unpark_vehicle()

    def get_manager(self):
        return self._manager
