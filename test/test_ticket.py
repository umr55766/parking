import unittest

from src.ticket import Ticket


class TicketTest(unittest.TestCase):
    @property
    def ticket_number(self):
        return 100

    def test_ticket_number(self):
        # Given
        ticket = Ticket()

        # When
        ticket.set_ticket_number(self.ticket_number)

        # Then
        self.assertEqual(ticket.get_ticket_number(), self.ticket_number)
