class Ticket:
    def __init__(self):
        self._number = 0

    def get_ticket_number(self):
        return self._number

    def set_ticket_number(self, number):
        self._number = number
