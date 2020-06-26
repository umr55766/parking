import unittest

from src.TicketSystem import TicketSystem
from src.ticket import Ticket


class TicketSystemTest(unittest.TestCase):
    def test_new_ticket_number(self):
        self.assertEqual(TicketSystem()._get_new_ticket_number(), 1)

    def test_generate_ticket(self):
        ticket_system = TicketSystem()
        ticket_system._last_ticket = Ticket()
        ticket_system._last_ticket.set_ticket_number(10)

        self.assertEqual(ticket_system.generate_ticket().get_ticket_number(), 11)