from django.test import TestCase
from unittest.mock import Mock

import stripe

from sync.models import Customer
import sync.views as v

import sync.harbor as h

class TestCustomer(TestCase):
    def test_creator(self):
        customer = Customer()
        self.assertEqual(customer.email, '')
        self.assertEqual(customer.stripe_id, '')

class TestViews(TestCase):
    def test_new_subscription(self):
        stripe.Customer.retrieve = Mock(return_value={'email':'customer@example.org'})
        customer_id = 'cus_Fg2W5cdlpF1oSs'
        subscription = {'customer': customer_id}

        self.assertEqual(len(Customer.objects.filter(stripe_id=customer_id)), 0)
        v.handle_new_subscription(subscription)
        self.assertEqual(len(Customer.objects.filter(stripe_id=customer_id)), 1)

class TestHarbor(TestCase):
    def test_customer_email_to_harbor_username(self):
        email = 'admin+plusaddress@example.org'
        username = h.customer_email_to_harbor_username(email)
        self.assertEqual(str.find(username, '@'), -1)
