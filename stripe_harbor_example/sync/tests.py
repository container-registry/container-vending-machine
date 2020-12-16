from django.test import TestCase
from unittest.mock import patch

from sync.models import Customer
import sync.views as v

class TestCustomer(TestCase):
    def test_creator(self):
        customer = Customer()
        self.assertEqual(customer.email, '')
        self.assertEqual(customer.stripe_id, '')

class TestViews(TestCase):
    def test_new_subscription(self):
        customer_id = 'cus_Fg2W5cdlpF1oSs'
        subscription = {'customer': customer_id}
        self.assertEqual(len(Customer.objects.filter(stripe_id=customer_id)), 0)
        v.handle_new_subscription(subscription)
        self.assertEqual(len(Customer.objects.filter(stripe_id=customer_id)), 1)
