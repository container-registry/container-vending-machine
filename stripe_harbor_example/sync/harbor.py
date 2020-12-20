import datetime
import requests
import json
import environ

env = environ.Env(DEBUG=(bool, False))


harbor_endpoint = 'https://' + env('HARBOR_HOST') + '/api/v2.0'

def harbor_get(path):
    return requests.get(
            harbor_endpoint + path,
            auth=(env('HARBOR_USERNAME'), env('HARBOR_PASSWORD')),
            headers={'Accept':'application/json'})

def harbor_post(path, data):
    return requests.post(
            harbor_endpoint + path,
            data=data,
            auth=(env('HARBOR_USERNAME'), env('HARBOR_PASSWORD')),
            headers={'Accept':'application/json'})

def get_robot_accounts_for_project():
    accounts = harbor_get('/projects/10/robots').json()

def create_robot_account_for_project():
    account = harbor_post(
            '/projects/10/robots',
            json.dumps({
                'name':'sample_name',
                'expires_at': int((datetime.datetime.now() + datetime.timedelta(days=30)).timestamp()),
                'access': [
                    {"resource":"/project/10/repository","action":"pull"},
                    {"resource":"/project/10/helm-chart","action":"read"}
                    ],
                })
            )
    return account.json()

def setup_harbor_client():
    harbor_host = env('HARBOR_HOST')
    harbor_username = env('HARBOR_USERNAME')
    harbor_password = env('HARBOR_PASSWORD')
    return harborclient.HarborClient(
            harbor_host, harbor_username, harbor_password)

#harbor_client = setup_harbor_client()

def create_harbor_user_from_customer(customer):
    if not self.customer_email:
        raise ValueError("Couldn't create harbor user for customer %s - the object doesn't have the email set" % (customer.id))
    generated_password = ''.join(
            random.sample(string.ascii_letters + string.digits, 16)),
    user = harbor_client.create_user(
            # use email as username for simplicity
            self_customer_email,
            self.customer_email,
            generated_password,
            # don't set a real name
            "",
            # don't set a comment
            "")
    # send email?
    return user

def provision_harbor_permissions_for_customer(customer):
    project_name = "software_product_repo"
    # add permissions
    return True

def remove_product_access_for_customer(customer):
    # remove product access
    return True
