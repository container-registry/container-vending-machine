from django.test import TestCase
from sync.models import Customer

class TestCustomer(django.test.TestCase):
    def test_creator(self):
        customer = Customer()
        self.assertEqual(customer.email, None)
        self.assertEqual(customer.stripe_id, None)
