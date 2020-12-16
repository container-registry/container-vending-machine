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

#def test_add_card_failure(self, retrieve_mock):
    #@patch('stripe.Customer.retrieve')
    #data = {
        #'name': "shubham",
        #'cvc': 123,
        #'number': "4242424242424242",
        #'expiry': "12/23",
    #}
    #e = CardError("Card Error", "", "")
    #retrieve_mock.return_value.sources.create.return_value = e

    #self.api_client.client.login(username=self.username, password=self.password)

    #res = self.api_client.post('/biz/api/auth/card/add', data=data)

    #self.assertEqual(self.deserialize(res)['success'], False)
