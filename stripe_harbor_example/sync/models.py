from django.db import models
import string
import stripe
import sync.harbor as h

class Customer(models.Model):
    email = models.CharField(max_length=70)
    name = models.CharField(max_length=70)
    stripe_id = models.CharField(max_length=70)

    def create_stripe_customer():
        if (not self.stripe_id) and self.customer_email:
            customer = stripe.Customer.create(email=customer_email)
            self.stripe_id = customer.id
            return self.stripe_id
        else:
            print("Could not create a Stripe customer")

    def ensure_email(self):
        if not self.email:
            self.email = stripe.Customer.retrieve(self.stripe_id)['email']

    def create_harbor_user(self):
        h.create_harbor_user_from_customer(self)

    def provision_product_access(self):
        h.provision_harbor_permissions_for_customer(self)

    def remove_product_access(self):
        h.remove_product_access_for_customer(self)
