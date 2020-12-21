# Integrating Stripe payments with a container registry

The purpose of this example is to show how a software vendor can integrate a subscription management service with a container registry with the purpose of distributing software as a container image.

## High-level summary of the example

Create Harbor robot accounts for your customers to allow them to pull your software from a Harbor registry.

* Receive [Stripe](https://stripe.com/billing) webhooks, use the information to create customer records in our own database.
* Provision access to a [Harbor](https://goharbor.io) repository, and remove access if a Stripe subscription expires.

The application is implemented using Python and Django. We use a managed Harbor registry provided by [Container Registry](https://container-registry.com).

## Limitations of the example

* We use the Subscription Expired webhook from Stripe to remove access to a Harbor account. A better way to do this would be to set an expiry date for a Harbor robot account, and to extend that date when an outstanding invoice is paid in Stripe.
* We don’t send the Harbor credentials — need to send them to customers through email.
* Harbor usernames are generated automatically from the customer’s email on the subscription and can’t be customized.
* Error handling is limited, both for Stripe and Harbor.
* The test coverage is basic and can be improved.

## The most interesting parts of the example

A lot of this example is basic Django code, the most valuable pieces with the business logic are:

* [`stripe_harbor_example/sync/harbor.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/harbor.py) for the Harbor actions over HTTP.
* [`stripe_harbor_example/sync/models.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/models.py) for the details of what we store in this application’s database.
* [`stripe_harbor_example/sync/tests.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/tests.py) for tests! Tests are useful.
* [`stripe_harbor_example/sync/views.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/views.py) for Stripe webhook handling.

## Running the example

Step 1: Create an environment file at `stripe_harbor_example/stripe_harbor_example/.env`. Here’s an example of the `.env` file’s content (remember to use your Stripe and Harbor credentials):

```shell
DEBUG=True
SECRET_KEY='django_secret_key'
STRIPE_API_KEY="sk_test_..."

HARBOR_USERNAME='meaning_of_life'
HARBOR_PASSWORD='42'
HARBOR_HOST='demo.goharbor.io'
```

Step 2: Install all required dependencies.

```shell
$ pip install -r requirements.txt
```

Step 3: Run the tests.

```shell
$ cd stripe_harbor_example
$ ./manage.py test
```

Step 4: Run the web server.

```shell
$ ./manage.py runserver
```

## Starting an interactive shell

Start an interactive shell with all dependencies and the environment pre-loaded.

```shell
$ ./manage.py shell
```


## Questions and issues

If you have a question or if you found a bug, please open a new issue on this repository.