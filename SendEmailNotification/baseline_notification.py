### Author:     Han Thu  	  ###
### Date:       March 15, 2019  ###
### Client:      ###
### Description:
###     Send email notification for Baseline Running    ###



#!/usr/bin/env python     ## Set interpreter used to be the one on your environment's $PATH
#import pyodbc
import time
import os
import datetime
import calendar
import pandas as pd
import pyodbc
from sqlalchemy import create_engine

### library for sending email notification ##
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename





class Mailer:
    def __init__(self):
        self.gmail_accnt = GMAIL_ACCNT
        self.pwd = GMAIL_PWD

    def send_email(self, recipients, subject, body, attachment=None):
        sender = self.gmail_accnt # FROM
        pwd = self.pwd
        to = SEPARATOR.join(recipients) if type(recipients) is list else recipients

        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = to
        msg.attach(MIMEText(body, 'html'))

        if attachment:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(attachment, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="' + basename(attachment) + '"')
            msg.attach(part)

        try:
            server = smtplib.SMTP("outlook.office365.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, pwd)
			# recipients needs to be a LIST whereas msg['To'] needs to be a string
			# http://stackoverflow.com/a/28203862
            server.sendmail(sender, recipients, msg.as_string())
            server.close()
        except Exception as err:
            print("Failed to send the email with this error:\n", err)


def main():
  #mymail = Mailer()
  server = smtplib.SMTP('smtp.office365.com',587)
  server.starttls()
  msg = MIMEMultipart()
  message = 'Subject: {}\n\n{}'.format("This is Subject", "This is body")
  msg.attach(MIMEText(message))
  server.login("han.thu@groupm.com","Harrison2k71990!@#$%")
  server.sendmail("han.thu@groupm.com", "hanminthu2007@gmail.com", message)
    

main()




