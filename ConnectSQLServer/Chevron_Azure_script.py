### Author:     Han Thu  	  ###
### Date:       December 25, 2018  ###
### Client:     Chevron (DM_1485,  10.2.186.181\SQLINS04,4723) ###
### Description:
### Comparing data for three main tables below  ###
###      - (Innovid)  [DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
###      - (Innovid)  [DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted]
###      - (Sizmek)   [DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
###  


#!/usr/bin/env python     ## Set interpreter used to be the one on your environment's $PATH
import pyodbc
import time
import pandas as pd
import os
import datetime
from datetime import date


"""
Handle datetime to str and print out in date format
https://github.com/mkleehammer/pyodbc/issues/329

def handleDateToString(dateObj):
    return dateObj.strftime('%H:%M:%S.%f')
"""

def ConnectAzure():
      global finaltable
      
      print ("Connecting 'Chevron' client on Azure")
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=wmdata-us.database.windows.net;DATABASE=WM-NA-Chevron;UID=DASuser;PWD=Passw0rd')
            ## Creating cursors to pull data from Chevron clients ##
      cursor1 = cnxn.cursor()   ## date cursor for "DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted"
      cursor2 = cnxn.cursor()   ## date cursor for "DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted"
      cursor3 = cnxn.cursor()   ## date cursor for "DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted"

            ########  Table 1  ########
            #### Creating list for <DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted> table
      list1 = ['DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted']
            ## Getting max date
      cursor1.execute(""" 
                SELECT MAX([Day])
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            #print(type(record[0]))
            list1.append(record[0])
            print("Max date in DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor1.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            list1.append(record[0])
            print("Total Rows: ",record[0])
      print("list1: ",list1)

            ########  Table 2  ########
            ####  Creating list for <DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted> table
      list2 = ['DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted']
            ## Getting total number of rows
      cursor2.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted]
      """)
      for record in cursor2:
            list2.append(record[0])
            print("Total Rows: ",record[0])
      print("list2: ",list2)

            ########  Table 3  ########
            #### Creating list for <DS020307_Sizmek_Device_Video_Report_Chevron_Extracted> table
      list3 = ['DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted']
            ## Getting max date
      cursor3.execute(""" 
                SELECT MAX([Date])
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            sep = ' '   ## create separator for converting smalldatetime to str
            list3.append(str(record[0]).split(sep,1)[0])
            print("Max date in DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor3.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            list3.append(record[0])
            print("Total Rows: ",record[0])
      print("list3: ",list3)




def ConnectandCheckMaxDate_In_Premise():
      
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.2.186.148\SQLINS02,4721;DATABASE=DM_1406_TRowePrice;UID=DASuser01;PWD=DASpassw0rd')
      cursor = cnxn.cursor() ## cursor for max date from DS020301_Sizmek
      cursor2 = cnxn.cursor()
      cursor3 = cnxn.cursor()

      ## Check max date from DS020301_Sizmek report
      cursor.execute(""" 
      SELECT MAX([DeliveryDate])
      FROM [DM_1406_TRowePrice].[dbo].[DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]
      """)

      for record in cursor:
        print("Max date in [DS020301] Sizmek Campaign Report: ",record[0])
      max_date = record[0]
      ### https://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
      print("Max date from ::: ",max_date.strftime('%d, %b, %y'))

      ## Check max date from DS020302_Sizmek Conversions report
      cursor2.execute(""" 
      SELECT MAX([ConversionDate])
      FROM [DM_1406_TRowePrice].[dbo].[DFID061544_DS020302_Sizmek_Conversion_Report_TRowePrice_Extracted]
      """)

      for record2 in cursor2:
        print("Max date in [DS020302] Sizmek Conversion Report: ",record2[0])
      max_date2 = record2[0]
      
      print("Max date from ::: ",max_date2.strftime('%d, %b, %y'))
      print("max date kaaaaaaa ::: ",max_date2.isoformat())

      ###   Checking Today and validate if today is Monday  ###
      #today = datetime.datetime.today()
      today = date.today()
      print("today:", today)      
      print('Max date from format: ',today.strftime('%d, %b, %y'))

      ################################################################################################
      ################################################################################################










def main():
      os.system('cls')  ## clear the screen windows
      ConnectAzure()
      #ConnectandCheckMaxDate_In_Premise()



main()

