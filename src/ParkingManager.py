from src.ParkingFullError import ParkingFullError


class ParkingManager:
    def __init__(self, ticket_system, managed_slots):
        self._ticket_system = ticket_system
        self._slots = managed_slots

    def park(self, vehicle):
        ticket = self._ticket_system.generate_ticket()
        vehicle.get_driver().assign_ticket(ticket)
        self.get_available_slot().park(vehicle)

    def get_slot_of(self, car):
        for slot in self._slots:
            if slot.get_parked_vehicle() is car:
                return slot

    def get_available_slot(self):
        available_slots = [slot for slot in self._slots if slot.get_parked_vehicle() is None]

        if len(available_slots) is 0:
            raise ParkingFullError

        return available_slots[0]

    def get_overview(self):
        return [[
            slot.get_serial_number(),
            slot.get_parked_vehicle().get_registration_number() if slot.get_parked_vehicle() else "",
            slot.get_parked_vehicle().get_color() if slot.get_parked_vehicle() else "",
        ] for slot in self._slots if slot.get_parked_vehicle()]

    def get_registration_numbers_of_car_with_color(self, color):
        return ", ".join([slot.get_parked_vehicle().get_registration_number() for slot in self._slots
                          if slot.get_parked_vehicle() and slot.get_parked_vehicle().get_color() == color])

    def get_slot_numbers_for_cars_with_colour(self, color):
        return ", ".join([str(slot.get_serial_number()) for slot in self._slots
                          if slot.get_parked_vehicle() and slot.get_parked_vehicle().get_color() == color])

    def get_slot_number_for_color_with_number(self, registration_number):
        found_slots = [slot for slot in self._slots
                       if slot.get_parked_vehicle()
                       and slot.get_parked_vehicle().get_registration_number() == registration_number]

        return found_slots[0].get_serial_number() if len(found_slots) != 0 else "Not found"
