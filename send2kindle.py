#!/usr/bin/python3
import sys
import os
from os.path import basename
import argparse
import json
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase 
from email import encoders 

def load_config():
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(cwd, 'config.json'), 'r') as f:
        try:
            config = json.load(f)
        except Exception as e:
            print("Error: Parse config.json failed. Please recheck config template")
            sys.exit(0)
    return config

def _get_smtp_server(email):
    if email.endswith("@gmail.com"):
        return ('smtp.gmail.com', 587)
    elif email.endswith("@outlook.com"):
        return ('smtp-mail.outlook.com', 587)
    elif email.endswith("@yahoo.com"):
        return ('smtp-mail.yahoo.com', 587)
    else:
        print("Error: Email not supported, only support Gmail, Outlook and Yahoo mail")
        sys.exit(0)

def send_to_kindle(files):
    config = load_config()
    sender_email = config["sender"]["email"]
    sender_password = config["sender"]["password"]
    smtp_server = _get_smtp_server(sender_email)

    msg = MIMEMultipart()
    msg['Subject'] = 'Send to Kindle using send2kindle'
    msg['From'] = sender_email
    for file_path in files:
        file_name = file_path.name
        with open(file_name, "rb") as f:
            part = MIMEApplication(f.read())
        part['Content-Disposition'] = 'attachment; filename="%s"' % basename(file_name)
        msg.attach(part)

    try:
        with smtplib.SMTP(*smtp_server) as s:
            print("Connecting to SMTP Server...")
            s.ehlo()
            s.starttls()
            print("Logging you in...")
            s.login(sender_email, sender_password)
            print("Log in successfully!")
            for device in config["devices"]:
                receiver_email = device["kindle_email"]
                device_name = device["name"]
                opt = input("Send to %s? y/[n] " % device_name)
                if opt in ['Y', 'y', '']:
                    msg['To'] = receiver_email
                    s.sendmail(sender_email, receiver_email, msg.as_string())
                    print("Send to %s successfully!" % device_name)

    except Exception as e:
        print("Error: Sending email exception: %s" % e)

if __name__ == '__main__':
    parser =  argparse.ArgumentParser()
    parser.add_argument(
        'files', type=argparse.FileType('r'), nargs='+', 
        help="Files to send in format: doc, docx, mobi, pdf,..."
    )
    args = parser.parse_args()
    send_to_kindle(args.files)