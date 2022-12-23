import datetime
import requests
import json
import environ
import logging as log
import json
from .MailerSendNewApiClientAPI import *

env = environ.Env(DEBUG=(bool, False))

harbor_endpoint = 'https://' + env('HARBOR_HOST') + '/api/v2.0'
harbor_projects_path = '/projects/'+env('HARBOR_PROJECT_ID')
harbor_project_path = '/project/'+env('HARBOR_PROJECT_ID')
harbor_robots_path = f'{harbor_projects_path}/robots'

def harbor_get(path):
    return requests.get(
            harbor_endpoint + path,
            auth=(env('HARBOR_USERNAME'), env('HARBOR_PASSWORD')),
            headers={'Accept':'application/json'})

def harbor_post(path, data):
    log.warning(f"UserName --> {env('HARBOR_USERNAME')}")
    return requests.post(
            harbor_endpoint + path,
            data=data,
            auth=(env('HARBOR_USERNAME'), env('HARBOR_PASSWORD')),
            headers={'Accept':'application/json'})

def get_robot_accounts_for_project():
    # [{'id': 1, 'name':'robot$account_name', 'disabled':False, ...},
    #  {'id': 4, 'name':'robot$account_name_2', ...}]
    return harbor_get(harbor_robots_path).json()

def create_robot_account_for_project(account_name,email,customer_name):
    account = harbor_post(
        harbor_robots_path,
        json.dumps(
            {
                'name': account_name,
                'expires_at': int(
                    (
                        datetime.datetime.now() + datetime.timedelta(days=30)
                    ).timestamp()
                ),
                'access': [
                    {
                        'resource': f'{harbor_project_path}/repository',
                        'action': 'pull',
                    },
                    {
                        'resource': f'{harbor_project_path}/helm-chart-version',
                        'action': 'read',
                    },
                ],
            }
        ),
    )

    account=account.json()
    print(account)
    send_email(account,email,customer_name)
    log.warning(account)
    return account

def customer_email_to_harbor_username(email):
    username = email
    for ch in ['@', '.', '+']:
        if ch in username:
            username = str.replace(username, ch, '_')

    return username

def create_harbor_user_from_customer(customer_email,strip_id,customer_name):
    if not customer_email:
        raise ValueError(
            f"Couldn't create a harbor user for customer {strip_id} - the record doesn't have the email set"
        )
    return create_robot_account_for_project(customer_email_to_harbor_username(customer_email),customer_email,customer_name)

def provision_harbor_permissions_for_customer(customer):
    # add permissions
    return True

def remove_product_access_for_customer(customer):
    # remove product access
    return True
