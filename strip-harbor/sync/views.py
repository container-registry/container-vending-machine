from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import environ
import stripe
env = environ.Env(DEBUG=(bool, False))
from sync.models import Customer
# def hello(request):
#     #return HttpResponse(status=200)
#     return HttpResponse('<h1>Hello i m in</h1>')

stripe.api_key = env('STRIPE_API_KEY')

def handle_new_subscription(subscription):
    customer = Customer.objects.get_or_create(
            stripe_id=subscription['customer'])[0]
    customer.ensure_email()
    customer.create_harbor_user()
    customer.save()

def handle_deleted_subscription(deleted_subscription):
    customer = Customer.objects.get(stripe_id=deleted_subscription['customer'])
    # don't remove the repo or the user yet, clean it up after a grace period
    customer.remove_product_access()

@csrf_exempt
def webhook_handler(request):
    payload = request.body
    event = None

    try:
        print("yes")
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key)
    except ValueError as e:
        return HttpResponse(status=400)

    if event.type == 'customer.subscription.created':
        #new_subscription=handle_new_subscription()
        print("Handle new subscription")
        new_subscription = event.data.object
        handle_new_subscription(new_subscription)

    elif event.type == 'customer.subscription.deleted':
        deleted_subscription = event.data.object
        handle_deleted_subscription(deleted_subscription)

    else:
        print(f'Unhandled event type {event.type}')

    return HttpResponse(status=200)