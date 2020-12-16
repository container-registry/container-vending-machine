from django.db import models
import string
import stripe

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

    def create_harbor_user():
        if self.customer_email:
            generated_password = ''.join(
                    random.sample(string.ascii_letters + string.digits, 16)),
            user = harbor.create_user(
                # use email as username for simplicity
                self_customer_email,
                self.customer_email,
                generated_password,
                # don't set a real name
                "",
                "Created through the Customer model")
            # send email to user

    def extend_account_validity():
        return None
