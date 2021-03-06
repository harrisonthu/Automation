### Author: Han Thu  	  ###
### Date: April 23, 2018  ###
### WEEKLY GUID File ###


#!/usr/bin/env python     ## Set interpreter used to be the one on your environment's $PATH
import pyodbc
import time
import os
import datetime
from datetime import date


"""
Handle datetime to str and print out in date format
https://github.com/mkleehammer/pyodbc/issues/329

def handleDateToString(dateObj):
    return dateObj.strftime('%H:%M:%S.%f')
"""



def ConnectandCheckMaxDate():
      global max_date
      global max_date2
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.2.186.148\SQLINS02,4721;DATABASE=DM_1406_TRowePrice;UID=DASuser01;PWD=Passw0rd')
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
        #print("this is under for loop")
      
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
      
      #Deleteprint("Max date from ::: ",max_date2.strftime('%d, %b, %y'))
      #Deleteprint("max date kaaaaaaa ::: ",max_date2.isoformat())

      ###   Checking Today and validate if today is Monday  ###
      #today = datetime.datetime.today()
      today = date.today()
      print("today:", today)      
      print('Max date from format: ',today.strftime('%d, %b, %y'))

      ################################################################################################
      ################################################################################################

      cursor3.execute("""


      SELECT CreativeGUID, 
            ClientName, 
            [AdvertiserName], 
            CreativeDescription 
      FROM   ( 
            -- Atlas feed 
            SELECT DISTINCT [Ad ID]           AS CreativeGUID, 
                        [Advertiser Name] AS ClientName, 
                        [Advertiser Name] AS [AdvertiserName], 
                        [Ad Name]         AS CreativeDescription 
            FROM   [DFID043910_DS999606_Email_Atlas_UI_Performance_Report_TRowePrice_Extracted] 
            WHERE  [Campaign Type] = 'Display' 
                  AND [Statistics Date] >= '2016-09-01' -- pull data from '2016-09-01'   
                  AND ( [Impressions] > '0' 
                        OR [clicks] > '0' ) 
                  AND [campaign name] NOT LIKE '%Yieldbot%' 
                  AND [campaign name] NOT LIKE 'FB_%' 
                  AND [campaign name] NOT LIKE '%_Social_%' 
                  AND [campaign name] NOT LIKE 'Instagram_%' 
                  AND [campaign name] NOT LIKE 'IG_%' 
                  -- Added by Han on 4/10/2018 (Leo requested to filter out campaign name --SEM-- (e.g TR_FIS_103_T Rowe Retirement Advisor_SEM_1H_2018) 
                  AND [campaign name] NOT LIKE '%SEM%' 
                  AND [campaign name] NOT IN ( 'TRP_APP_Q4_2017_UM_ Retargeting', 'TRP_APP_Q4_2017_UM_Referral', 'TRP_APP_Q4_2017_UM_VideoViews', 'TRP_II_Q4_2017_UM_ Retargeting', 
                                                'TRP_II_Q4_2017_UM_Referral', 'TRP_II_Q4_2017_UM_VideoViews' ) 
            UNION ALL 
            -- Sizmek feed 
            SELECT DISTINCT Cast([AdID] AS NVARCHAR(50)), 
                              CASE 
                              WHEN [AdvertiserName] = 'TRowe Price' THEN 'T. Rowe Price' 
                              ELSE [AdvertiserName] 
                              END AS [ClientName], 
                              CASE 
                              WHEN [AdvertiserName] = 'TRowe Price' THEN 'T. Rowe Price' 
                              ELSE [AdvertiserName] 
                              END AS [AdvertiserName], 
                              [AdName] 
            FROM   [dbo].[DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted] 
            WHERE  [DeliveryDate] >= '2017-10-02' -- pull data from '2016-09-01'   
                  AND ( [Impressions] > '0' 
                        OR [clicks] > '0' ) 
                  AND [campaignname] NOT LIKE '%Yieldbot%' 
                  AND [campaignname] NOT LIKE 'FB_%' 
                  AND [campaignname] NOT LIKE '%_Social_%' 
                  AND [campaignname] NOT LIKE 'Instagram_%' 
                  AND [campaignname] NOT LIKE 'IG_%' 
                  AND [campaignname] NOT LIKE '%Q3 2017%' 
                  -- Added by Han on 4/10/2018 (Leo requested to filter out campaign name --SEM-- (e.g TR_FIS_103_T Rowe Retirement Advisor_SEM_1H_2018) 
                  AND [campaignname] NOT LIKE '%SEM%' 
                  AND [campaignname] NOT IN ( 'TRP_APP_Q4_2017_UM_ Retargeting', 'TRP_APP_Q4_2017_UM_Referral', 'TRP_APP_Q4_2017_UM_VideoViews', 'TRP_II_Q4_2017_UM_ Retargeting', 
                                                'TRP_II_Q4_2017_UM_Referral', 'TRP_II_Q4_2017_UM_VideoViews' )) FOO 


            """)
      #print(cursor3)
      #print(type(cursor3))
      #result = cursor3.fetchall()
      #print("result: ",result)
      #while result:
       #     print(str(result[0]) + result[1] + " lives in " + result[2] + "last column"+ result[3])      
      ################################################################################################
      ################################################################################################

def ChecktodayMonday():
      istodaymonday = date.today().weekday()
      print("istodaymonday:",istodaymonday)
      if (istodaymonday ==0): #check today monday
            return 1
      else:
            return 0
                  #if istodaymonday==2:
      #      global Trigger = True ## check if today monday

      
def TriggerandRunWEEKLYCreativeGUID_DE104():
      print("haha")
      
      
      


def main():
      os.system('cls')  ## clear the screen windows
      ConnectandCheckMaxDate()
      if (ChecktodayMonday() ==1):
            TriggerandRunWEEKLYCreativeGUID_DE104()
      else:
            user_input = input("Today is not Monday, do you want to export WEEKLY GUID file?: Press 'y' for 'Yes',otherwise 'n' for 'No' ").lower()
            if (user_input == 'y'): # force to run WEEKLY GUID
                  TriggerandRunWEEKLYCreativeGUID_DE104()
            else:    # Not going to run WEEKLY GUID
                  print("Thank you for running this WEEKLY GUID file. Have a nice day !  :)")
      
      



main()

