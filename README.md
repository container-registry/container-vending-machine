# The Container Vending Machine 
or how to integrate Stripe with a container registry and sell your software.

The purpose of this example is to show how a software vendor can integrate a subscription management service with a container registry with the purpose of distributing software as a container image.

## High-level summary of the example

Create Harbor robot accounts for your customers to allow them to pull your software from a Harbor registry.

* Receive [Stripe](https://stripe.com/billing) webhooks, use the information to create customer records in our own database.
* Provision access to a [Harbor](https://goharbor.io) repository, and remove access if a Stripe subscription expires.

The application is implemented using Python and Django. We use a managed Harbor registry provided by [Container Registry](https://container-registry.com).

## Limitations of the example

* We use the Subscription Expired webhook from Stripe to remove access to a Harbor account. A better way to do this would be to set an expiry date for a Harbor robot account, and to extend that date when an outstanding invoice is paid in Stripe.
* We send the Harbor credentials to customers through email.
* Harbor usernames are generated automatically from the customer’s email on the subscription and can’t be customized.
* Error handling is limited, both for Stripe and Harbor.

## The most interesting parts of the example

A lot of this example is basic Django code, the most valuable pieces with the business logic are:

* [`stripe_harbor_example/sync/harbor.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/harbor.py) for the Harbor actions over HTTP.
* [`stripe_harbor_example/sync/models.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/models.py) for the details of what we store in this application’s database.
* [`stripe_harbor_example/sync/views.py`](https://github.com/chief-wizard/stripe-harbor-example/blob/master/stripe_harbor_example/sync/views.py) for Stripe webhook handling.

## Running the example
```
Requirements:-

-faas-cli
-Docker
-Stripe
```
Step 1: Create an environment file at `Stripe Harbor Example/stripe_harbor/strip_harbor_api/.env`. Here’s an example of the `.env` file’s content (remember to use your Stripe and Harbor credentials):

```shell
DEBUG=True
SECRET_KEY='secret key'
STRIPE_API_KEY='api key'
HARBOR_HOST='io.com'
HARBOR_USERNAME='x'
HARBOR_PASSWORD='xxxx'
HARBOR_PROJECT_ID='xxxx'
MAILERSEND_API_KEY="xxxxx"
FROM_EMAIL="abc@gmail.com"
TEMPLATE_ID="xxxx"
ACCOUNT_NAME="example"
SUPPORT_EMAIL="example@xx.com"
```

Step 2:

1. Login into Docker

```shell
$ docker login <server> --username <user> --password-stdin
```

2. Login into Faas-cli

```shell
$ faas-cli login -g <gateway> -u <username> -p <password>
```

Step 3:

Build the Docker Image
```
 Make changes in 'strip-harbor.yml file' for Function and Image(FQDN)  
```

```shell
$ faas-cli build -f <filename.yml> 
```

Step 4:

Push the Docker Image
```shell
$ docker push <image name>
``` 
Step 5:

Deploy the Image into Openfaas(for that change gateway in 'strip-harbor.yml file' )
```shell
$ faas-cli deploy <filename.yml>
```
Step 6:

1 . Create webhook in stripe(https://dashboard.stripe.com/test/webhooks)

2. Create Stripe Customer(for Local testing please install strip cli)

Navigate to Downloaded Strip Folder(For Local Testing)
```shell
$ ./stripe customers create --email=<email_id> --name=<name>
```

2. Create Subscription for the Customer
```shell
$ ./stripe subscriptions create --customer=<customer_id> -d "items[0][price]"=<price_id>
```

## Questions and issues

If you have a question or if you found a bug, please open a new issue on this repository.
