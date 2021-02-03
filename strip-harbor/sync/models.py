from django.db import models
import string
import environ
import stripe
import logging as log
import sync.harbor as h
import json

env = environ.Env(DEBUG=(bool, False))
stripe.api_key = env('STRIPE_API_KEY')


class Customer(models.Model):
    email = models.CharField(max_length=70, null=True)
    name = models.CharField(max_length=70, null=True)
    stripe_id = models.CharField(max_length=70, null=True)
    harbor_login = models.CharField(max_length=70, null=True)

    def create_stripe_customer(self):
        if (not self.stripe_id) and self.email:
            customer = stripe.Customer.create(email=self.email)
            self.stripe_id = customer.id
            return self.stripe_id
        else:
            print("Could not create a Stripe customer")

    def ensure_email(self):
        if not self.email or not self.name:
            cust_data = stripe.Customer.retrieve(self.stripe_id)
            self.email = cust_data['email']
            self.name = cust_data['name']

    def create_harbor_user(self):
        harbor_account = h.create_harbor_user_from_customer(self.email, self.stripe_id, self.name)
        self.harbor_login = harbor_account['name']
        self.save()
