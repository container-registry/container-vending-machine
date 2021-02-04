import mailersend
import os
import environ
import  logging as log
import json
import requests

env = environ.Env(DEBUG=(bool, False))

API_BASE = "https://api.mailersend.com/v1"

class MailerSendNewApiClient:
    def __init__(
        self,
        api_base=API_BASE,
        headers_default=None,
        headers_auth=None,
        mailersend_api_key=None,
    ):

        self.mailersend_api_key = env("MAILERSEND_API_KEY")
        if not self.mailersend_api_key:
            self.mailersend_api_key=mailersend_api_key
        self.headers_auth = "Bearer {}".format(self.mailersend_api_key)
        self.headers_default = {
            "Content-Type": "application/json",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "MailerSend-Client-python-v1",
            "Authorization": self.headers_auth,
        }


    def send(self, mail_from, mail_to, mail_subject, mail_content, mail_text=None,template_id=None, variables=None):
        self.mail_from = {"from": {"email": mail_from}}
        mail_data = [{"email": receiver} for receiver in mail_to]
        self.mail_to = {"to": mail_data}
        self.template_id={"template_id":template_id}
        self.mail_subject = {"subject": mail_subject}
        # self.mail_content = {"html": mail_content}
        self.variables={"variables":[{"email":mail_to[0], "substitutions":variables }]}
        self.mail_text = {"text": mail_text or "foo"}

        message = {
            **self.mail_from,
            **self.mail_to,
            **self.mail_subject,
            # **self.mail_content,
            # **self.mail_text,
            **self.template_id,
            **self.variables
        }

        print(json.dumps(self.headers_default))
        print(json.dumps(message))

        request = requests.post(
            API_BASE + "/email", headers=self.headers_default, json=message
        )
        return request.text


def send_email(takes,email,name):
    try:
        mailer = MailerSendNewApiClient(mailersend_api_key=env('MAILERSEND_API_KEY'))
        from_mail = env('FROM_EMAIL')
        template_id = env('TEMPLATE_ID')
        account_name = env('ACCOUNT_NAME')
        support_email = env('SUPPORT_EMAIL')
        hostname = env('HARBOR_HOST')
        username = takes['name']
        password = takes['token']
        subscriber_list = [email]
        subject = "Hello from container.ltd!"
        text = "Welcome to 8gears.com"

        variable= [{
                  "var": "user",
                  "value": username
                },
                {
                  "var": "password",
                  "value": password

                },{
                  "var": "hostName",
                  "value": hostname
                },{

                 "var": " account.name",
                  "value": account_name

                },{
                "var" : "support_email",
                "value" : support_email
            }]
        mailer.send(from_mail, subscriber_list, subject, '', text, template_id, variable)
    except Exception as e:
        log.warning(str(e))
        print("Sorry Failed to send the mail..Please contact admin for issue")


