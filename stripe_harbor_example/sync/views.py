from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from sync.models import Customer

import stripe
stripe.api_key = "sk_test_WCDAe6Ol0ufWlTxkvRw8JhRt00NguuRhXG"

def handle_new_subscription(subscription):
    customer = Customer.objects.get_or_create(
            stripe_id=subscription['customer'])
    customer.create_harbor_user()
    customer.provision_product_access()
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
        event = stripe.Event.construct_from(
                json.loads(payload), stripe.api_key)
    except ValueError as e:
        return HttpResponse(status=400)

    if event.type == 'customer.subscription.created':
        new_subscription = event.data.object
        handle_new_subscription(new_subscription)
    elif event.type == 'customer.subscription.deleted':
        deleted_subscription = event.data.object
        handle_deleted_subscription(deleted_subscription)
    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)

