import unittest

from src.Driver import Driver
from src.ticket import Ticket


class DriverTest(unittest.TestCase):
    def test_allot_ticket(self):
        # Given
        driver = Driver()
        ticket = Ticket()
        ticket.set_ticket_number(100)

        # When
        driver.assign_ticket(ticket)

        # Then
        self.assertEqual(driver._tickets[-1], ticket)
