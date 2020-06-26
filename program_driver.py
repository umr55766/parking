from src.Car import Car
from src.Driver import Driver
from src.Parking import Parking
from src.ParkingFullError import ParkingFullError

parking = None


def create_parking_lot(_, slot_count):
    global parking
    parking = Parking(int(slot_count))
    print("Created a parking lot with %s slots" % slot_count)


def park(_, registration_number, color):
    car = Car(registration_number, color)
    car.set_driver(Driver())
    try:
        parking.get_manager().park(car)
        print("Allocated slot number: %d" % parking.get_manager().get_slot_of(car).get_serial_number())
    except ParkingFullError:
        print("Sorry, parking lot is full")


def leave(_, slot_serial_number):
    parking.get_slot_by_serial_number(int(slot_serial_number)).unpark_vehicle()
    print("Slot number %s is free" % slot_serial_number)


def status(_):
    heading = ["Slot", "Registration No.", "Color"]
    overview = parking.get_manager().get_overview()
    row_format = "{:>20}" * (len(heading) + 1)
    print(row_format.format("", *heading))
    for row in overview:
        print(row_format.format("", *row))


def registration_numbers_for_cars_with_colour(_, color):
    print(parking.get_manager().get_registration_numbers_of_car_with_color(color))


def slot_numbers_for_cars_with_colour(_, color):
    print(parking.get_manager().get_slot_numbers_for_cars_with_colour(color))


def slot_number_for_registration_number(_, registration_number):
    print(parking.get_manager().get_slot_number_for_color_with_number(registration_number))


VALID_COMMANDS = {
    "create_parking_lot": create_parking_lot,
    "park": park,
    "leave": leave,
    "status": status,
    "registration_numbers_for_cars_with_colour": registration_numbers_for_cars_with_colour,
    "slot_numbers_for_cars_with_colour": slot_numbers_for_cars_with_colour,
    "slot_number_for_registration_number": slot_number_for_registration_number,
}

arguments = input().split(" ")

while arguments[0] in VALID_COMMANDS:
    VALID_COMMANDS[arguments[0]](*arguments)
    arguments = input().split(" ")
