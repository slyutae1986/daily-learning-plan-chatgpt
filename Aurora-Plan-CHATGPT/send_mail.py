import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Gmail API 所需权限
SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# 定位 credentials 和 token 路径
CREDENTIALS_PATH = os.path.join('credentials', 'credentials.json')
TOKEN_PATH = os.path.join('credentials', 'token.json')

def get_gmail_service():
    creds = None
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    else:
        flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_PATH, SCOPES)
        creds = flow.run_local_server(port=0)
        with open(TOKEN_PATH, 'w') as token_file:
            token_file.write(creds.to_json())
    service = build('gmail', 'v1', credentials=creds)
    return service

def create_message(sender, to, subject, body_text):
    message = MIMEText(body_text, 'html')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(sender, to, subject, body_text):
    service = get_gmail_service()
    message = create_message(sender, to, subject, body_text)
    try:
        sent_message = service.users().messages().send(userId='me',
