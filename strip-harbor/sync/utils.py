import mailersend
import os
import environ
import  logging as log
env = environ.Env(DEBUG=(bool, False))

def send_email(takes,email,name):
    try:
        mailer = mailersend.NewApiClient(mailersend_api_key=env('MAILERSEND_API_KEY'))
        subject = "Welcome to 8gears.com"
        text = "Harbor Credentials"
        username = takes['name']
        password = takes['token']
        if not name:
            name = email
        html = "Hi ,<b>%s</b> <br> <p style='line-height: 0.5'>Here is your user name and password for the harbor login." \
           "</p><br><p style='line-height: 0.8'>username:%s <br><br><br>password:%s <br></p>please don't share it with any one!<br><br><br>" \
            "<b>Thanks!</b><br><h3>8gearscom</h3>" % (name,username,password)
        my_mail = env('FROM_EMAIL')
        subscriber_list = [email]
        mailer.send(my_mail, subscriber_list, subject, html, text)
    except Exception as e:
        log.warning(str(e))
        print("Sorry Failed to send the mail..Please contact admin for issue")
