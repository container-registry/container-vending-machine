import mailersend
import os
import environ
import  logging as log
env = environ.Env(DEBUG=(bool, False))



import json
import os
import requests

API_BASE = "https://api.mailersend.com/v1"

class MailerSendNewApiClient:
    def __init__(
        self,
        api_base=API_BASE,
        headers_default=None,
        headers_auth=None,
        mailersend_api_key=None,
    ):

        self.mailersend_api_key = os.environ.get("MAILERSEND_API_KEY")
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

        self.variables={"variables":[{"email":mail_to[0], "substitutions":
            variables }]}

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

# mailer = MailerSendNewApiClient(mailersend_api_key="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIxIiwianRpIjoiYjRhMjEwY2E3NGE4ZWQxMGQ5YmFiYzdjNjE0MTUyNDcyZjVhZjYyMDc0MDJlYmJiMWY3NGJlYWYwODM3NDVkMWI2YTdmZmFiYTNiYWVmNjEiLCJpYXQiOjE2MTIyNTUzNjIsIm5iZiI6MTYxMjI1NTM2MiwiZXhwIjo0NzY3OTI4OTYyLCJzdWIiOiIxMjAiLCJzY29wZXMiOlsiZW1haWxfZnVsbCIsImRvbWFpbnNfcmVhZCIsImFjdGl2aXR5X3JlYWQiLCJhbmFseXRpY3NfcmVhZCIsInRlbXBsYXRlc19mdWxsIl19.aaXc1WfVrOWut7qlu1Lz3RD_srhKEWoAytQ3JHJlcv2emxIEafLpKpAdejj1eNtkup2brtLFkTmerVFVhM3gdkKBjpV1Vwp1hqifRpJstlv3vokpNbvBFkMtvPvtMQf1AV5jI3tu9efztIcd53jcqwnke-R0mpvUuxB-yzryZaX0u23DppdD1rM3u3U1mga3fmt3wTUUgsriec2xYtU13w3QoDw0Ts5hFpGpZPS2j7c_csPHpeOjQpd1WJTaAKuyll4XrEK78x23Lvz8xoejDj1D6nffk7-XXdJwbJNUWPSQiwUz2ldxj1U-DAGrXg_OvIKYXvUeQnbv6oRNJuPFrLKY3TnzdCn30mS5vj0V_PQGrJF_E2B_MXEiJ1uzDlBE6JUpc0OPmw24Sulk7P0lxhbyflksBzRUDXv8aGvPe9BsVAIZ97yvaAonhsReBhf4cAjzDgVpMNdQyUHzX2WEfyR1mNDDeOIqvbt1J_B4qgy-1DdjosrQekvo3Yf1RtDcHJWDQjyYO2eW9tRKWs-j9J4MxqTlCHidjawscvYrRnFdwRb9ZeqgRL2UlVtWDQLZ4xx8GG4rVUl_lCu4wqqj4GswUx3xcf3QD87I_UtGZacYzkkrq2xzbD2MyqjgcsZ8wWQQ2HYwxqOhzhxny3_Iv4wz4IcAFpI071Mv6wK8iJ4")
# dict= [{
#           "var": "user",
#           "value": "test"
#         },
#         {
#           "var": "password",
#           "value": "12132132"
#
#         },{
#
#          "var": " account.name",
#           "value": "Hey"
#
#         }]
# mailer.send("no-reply@container-registry.com", ["tarunsengar1987@gmail.com"], "Hello from container.ltd!", '', "welcome","z86org89qk4ew137",dict)







def send_email(takes,email,name):
    try:
        mailer = MailerSendNewApiClient(mailersend_api_key=env('MAILERSEND_API_KEY'))
        from_mail = env('FROM_EMAIL')
        template_id=env('TEMPLATE_ID')

        # subject = "Welcome to 8gears.com"
        # text = "Harbor Credentials"
        #username = takes['name']
        #password = takes['token']
        # if not name:
        #     name = email
        # html = "Hi ,<b>%s</b> <br> <p style='line-height: 0.5'>Here is your user name and password for the harbor login." \
        #    "</p><br><p style='line-height: 0.8'>username:%s <br><br><br>password:%s <br></p>please don't share it with any one!<br><br><br>" \
        #     "<b>Thanks!</b><br><h3>8gearscom</h3>" % (name,username,password)
        # my_mail = env('FROM_EMAIL')
        # subscriber_list = [email]
        #mailer.send(my_mail, subscriber_list, subject, html, text)

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

                 "var": " account.name",
                  "value": '8gears'

                }]
        MailerSendNewApiClient.send(from_mail, subscriber_list, subject, '', text, template_id, variable)
    except Exception as e:
        log.warning(str(e))
        print("Sorry Failed to send the mail..Please contact admin for issue")


