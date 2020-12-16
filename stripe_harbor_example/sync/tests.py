from django.test import TestCase

from sync.models import Customer

class TestCustomer(TestCase):
    def test_creator(self):
        customer = Customer()
        self.assertEqual(customer.email, '')
        self.assertEqual(customer.stripe_id, '')
