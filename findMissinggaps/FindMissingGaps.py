### Author:     Han Thu  	  ###
### Date:       February 06, 2019  ###
### Client:     T Rowe Price (DM_1406,  10.2.186.148\SQLINS02) ###
### Description:
### Finding the missing data gaps in the three tables names below ###
### Print out the missing dates' data  ###
### Push out in excel/csv format categorizing sheets according to three data sources below ###
###      - (IAS)      [DFID052284_DS999622_FTP_IAS_TRP_Extracted]
###      - (Adobe)    [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]
###      - (Sizmek)   [DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]


#!/usr/bin/env python     ## Set interpreter used to be the one on your environment's $PATH
#import pyodbc
import time
import os
import datetime
import xlsxwriter
import pandas as pd
from sqlalchemy import create_engine


"""
  Function to connect the Server Name
  so that the other function can access and use the connection
"""
def Connection():
  Connection.ServerName = "10.2.186.148\SQLINS02"
  Connection.Database = "DM_1406_TRowePrice"
  Connection.UserPwd = "DASuser01:DASpassw0rd"
  Connection.Driver = "driver=SQL Server Native Client 11.0"
  # Create the connection
  print('Connecting ' + Connection.Database + ' Database ...')
  Connection.engine = create_engine('mssql+pyodbc://' + Connection.UserPwd + '@' + Connection.ServerName + '/' + Connection.Database + "?" + Connection.Driver)



"""
    Checking data gaps based on the dates that the table is missing:
    Retrieving data and add it in 
"""
def getIASTable():
  """
  Function to pull the table From In-Premise table
  using Panda library(read_sql) 
  """
  
  maxsql = """
        SELECT MAX([Date])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]
        """

  ##  Connecting IAS
  ##  List out all the missing dates
  sql = """
        SELECT
        DayInBetween AS missingDate
        FROM dbo.GetAllDaysInBetween('2019-01-01', 
	----  Find the Max date in the table/view
	(SELECT MAX([Date])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted])
	) AS AllDaysInBetween
	----  END: Find the Max date in the table/view
        WHERE NOT EXISTS 
        (SELECT [adserver id] FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted] WHERE [Date] = AllDaysInBetween.DayInBetween)
        """
  print("Connected ", Connection.Database)
  print("Finding Missing data gaps in Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted] ...")
  then = time.time() # Time before the operations start
  IASdf = pd.read_sql(sql, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  maxdateIAS = pd.read_sql(maxsql, Connection.engine)
  #df['DOB1'] = df['DOB'].dt.strftime('%m/%d/%Y')
  #print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: "+ maxdateIAS.to_datetime(datetime))
  print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", maxdateIAS.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds")
  return IASdf


def getAdobeTable():
  
  maxsql = """
        SELECT MAX([Date])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted]
        """

  ##  Connecting IAS
  ##  List out all the missing dates
  sql = """
        SELECT
        DayInBetween AS missingDate
        FROM dbo.GetAllDaysInBetween('2019-01-01', 
	----  Find the Max date in the table/view
	(SELECT MAX([Date])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted])
	) AS AllDaysInBetween
	----  END: Find the Max date in the table/view
        WHERE NOT EXISTS 
        (SELECT [adserver id] FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted] WHERE [Date] = AllDaysInBetween.DayInBetween)
        """
  print("Connected ", Connection.Database)
  print("Finding Missing data gaps in Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted] ...")
  then = time.time() # Time before the operations start
  IASdf = pd.read_sql(sql, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  maxdateIAS = pd.read_sql(maxsql, Connection.engine)
  #df['DOB1'] = df['DOB'].dt.strftime('%m/%d/%Y')
  #print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: "+ maxdateIAS.to_datetime(datetime))
  print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", maxdateIAS.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds")
  return IASdf





def main():
  Connection()
  getIASTable()


main()
