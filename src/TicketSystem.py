from src.ticket import Ticket


class TicketSystem:
    def __init__(self):
        self._last_ticket = None

    def _get_new_ticket_number(self):
        if self._last_ticket is None:
            return 1

        return self._last_ticket.get_ticket_number() + 1

    def generate_ticket(self):
        new_ticket = Ticket()
        new_ticket.set_ticket_number(self._get_new_ticket_number())
        self._last_ticket = new_ticket
        return new_ticket
