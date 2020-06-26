from src.CarParkingSlot import CarParkingSlot
from src.TicketSystem import TicketSystem


class Parking:
    def __init__(self, slots):
        self._slots = [CarParkingSlot(_) for _ in range(1, slots+1)]
        self._ticket_system = TicketSystem()
