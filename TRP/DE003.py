### Author:     Han Thu  	  ###
### Date:       March 31, 2019  ###
### Client:      ###
### Description:
###     Send DE003 is running       ###



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



"""
  Function to connect the Server Name
  so that the other function can access and use the connection
"""
def Connection():
  Connection.ServerName = "10.2.186.148\SQLINS02"
  Connection.Database = "DM_1406_TRowePrice"
  Connection.UserPwd = "DASuser01:Passw0rd"
  Connection.Driver = "driver=SQL Server Native Client 11.0"
  # Create the connection
  print('Connecting ' + Connection.Database + ' Database ...')
  try:
      Connection.engine = create_engine('mssql+pyodbc://' + Connection.UserPwd + '@' + Connection.ServerName + '/' + Connection.Database + "?" + Connection.Driver)
  except ValueError:
      print("Oops ! That was no valide number . Try again ...")
  except Exception as err:
      print("Failed to connect with this error:\n", err)



"""
Check Status of DE003

"""
def DE003status():
  sql_create_log = """
        EXEC [dbo].[Han_DE003status]
        """
    
  sql_status = """
          SELECT [Flag]
          FROM [DM_1406_TRowePrice].[dbo].[baseline_Flag]
          WHERE [Step] LIKE '%COMPLETE%'
          """

  try:
    createlog = pd.read_sql(sql_create_log, Connection.engine)
    status = pd.read_sql(sql_status,Connection.engine)
  except Exception as err:
    print("Failed to connect with this error:\n", err)

  DE003status.res = status.loc[0,'Flag']
  #### Check whether u should run DE003 or not  ####
  if int(DE003status.res)== 0:
    return 0
  elif int(DE003status.res)  == 1:
    return 1
  else:
    return True



def DE003run():
  
  sql_spone = """  EXEC [dbo].[Han_Testing]
        """
  sql_sptwo = """
        EXEC [dbo].[Han_Testing_v2]
        """
  sql_spthree = """
        EXEC [dbo].[Han_Testing]
        """
  sql_spfour = """
        EXEC [dbo].[Han_Testing_v2]
        """
  print("DE003 is currently running ... \n")
  DE003run.result1 = pd.read_sql(sql_spone, Connection.engine)
  print("Mapping Table <Step 1/4> is complete") 
  
  DE003run.result2 = pd.read_sql(sql_sptwo, Connection.engine)
  print("Normalization Generic <Step 2/4> is complete") 

  DE003run.result3 = pd.read_sql(sql_spthree, Connection.engine)
  print("Conversions Generic <Step 3/4> is complete \n") 

  DE003run.result4 = pd.read_sql(sql_spfour, Connection.engine)
  print("DE003 is successfully completed ! ") 

  return True


"""


SEPARATOR = ', '

class Mailer:
    def __init__(self):
        self.gmail_accnt = "sonyadasteam@gmail.com"
        self.pwd = "DASpassw0rd"

    def send_email(self, recipients, subject, body, attachment=None):
        sender = self.gmail_accnt # FROM
        pwd = self.pwd
        to = SEPARATOR.join(recipients) if type(recipients) is list else recipients
        ## calling BaseLine class
        myBL = BaseLine()
        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Baseline Status"
        msg['From'] = self.gmail_accnt
        msg['To'] = str(recipients)
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if myBL.StatusBaseline.result == 0:
            msg.attach(MIMEText("Baseline is complete/not currently running ", 'html'))
        elif myBL.StatusBaseline.result == 1:
            msg.attach(MIMEText("Baseline is currently running now at " + str(currenttime) + " ! ", 'html'))
        elif myBL.StatusBaseline.result == 2:
            msg.attach(MIMEText("Baseline is stuck since it has been running for over 3 hours from " + str(currenttime) + " ! ", 'html'))
        else:
            msg.attach(MIMEText("Baseline is currently running now at " + str(currenttime) + " ! ", 'html'))
        
        if attachment:
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(attachment, "rb").read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="' + basename(attachment) + '"')
            msg.attach(part)

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login(sender, pwd)
			# recipients needs to be a LIST whereas msg['To'] needs to be a string
			# http://stackoverflow.com/a/28203862
            server.sendmail(sender, recipients, msg.as_string())
            server.close()
        except Exception as err:
            print("Failed to send the email with this error:\n", err)


"""

"""
  Testing Function

def Testing():
  a = Mailer()
  recipients = [ 'han.thu@groupm.com'] ## add recipients emails 'bhumika.bhandari@groupm.com'
  SendingEmailNotificationForStarting.msg = MIMEMultipart()
  a.send_email(recipients,"this is my subject", "This is my body !")

"""



def SendingEmailNotificationForStarting():
    ## Server domain name, for google = smtp.gmail.com
    try:
      SendingEmailNotificationForStarting.server = smtplib.SMTP('smtp.gmail.com',587)
      SendingEmailNotificationForStarting.server.starttls()
      SendingEmailNotificationForStarting.msg = MIMEMultipart()
      #SendingEmailNotificationForStarting.currenttime = datetime.datetime.now()
      recipients = [ 'han.thu@groupm.com','hanminthu2007@gmail.com'] ## add recipients emails 'bhumika.bhandari@groupm.com'
      SendingEmailNotificationForStarting.message = 'Subject: {}\n\n{}'.format("Notification for status of DE003 for " + Connection.Database , "DE003 is just complete running ! " )
      SendingEmailNotificationForStarting.msg.attach(MIMEText(SendingEmailNotificationForStarting.message))
      SendingEmailNotificationForStarting.server.login("sonyadasteam@gmail.com","DASpassw0rd")
      SendingEmailNotificationForStarting.server.sendmail("sonyadasteam@gmail.com", recipients, SendingEmailNotificationForStarting.message)
      SendingEmailNotificationForStarting.server.close()
    except:
      print ("Something went wrong with this error ! \n",err)


def main():
    Connection()
    DEresult = DE003status()
    useryeslist = ["yes","y","ye","Y"]
    ###   DE003 is not currently running !  ###
    if int(DEresult) == 0:
      print("DE003 is not currently running ! ")
      userinput = input("Do you want to run DE003 now? 'Y'(or) 'Yes' to run: ").lower().strip()
      if(userinput in useryeslist):
        DE003run()
        SendingEmailNotificationForStarting()
      else:
        print("You can eixt the application now !\n")

    ###   DE003 is currently running !  ###
    elif int(DEresult) ==1:
      print("DE003 is currently running now. Please try again running later")
    os.system("pause")
    input("Press Enter to terminate the program: ")
    

    
"""
Main Function to run all of the functions/methods for this program"
"""
main()
