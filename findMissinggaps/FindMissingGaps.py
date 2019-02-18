### Author:     Han Thu  	  ###
### Date:       February 12, 2019  ###
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
  print("Connected ", Connection.Database, "!")


"""
    Checking data gaps from Jan 01, 2019 from  the table is missing:
    Retrieving data and add it in 
"""
def getIASTable():
  """
  Function to pull the Adobe table(DS999622_FTP_IAS_TRP_Extracted)
      - print out the max data from the table
      - is there any missing date from the table 
  """
  
  maxsql = """
        SELECT MAX([Date])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052284_DS999622_FTP_IAS_TRP_Extracted]
        """

  ##  Connecting IAS Table (DS999622_FTP_IAS_TRP)
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
  print("Finding Missing data gaps in Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted] ...")
  then = time.time() # Time before the operations start
  IASdf = pd.read_sql(sql, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  maxdateIAS = pd.read_sql(maxsql, Connection.engine)
  #df['DOB1'] = df['DOB'].dt.strftime('%m/%d/%Y')
  #print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ",maxdateIAS)
  print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", maxdateIAS.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds\n")
  return IASdf


def getAdobeTable():
  """
  Function to pull the Adobe table(DS999621_Email_Omniture_TRP_US_Extracted)
      - print out the max data from the table
      - is there any missing date from the table 
  """
  maxsql_adobe ="""
        SELECT MAX([Day])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]
        """

  ##  Connecting Adobe Table (DS999622_FTP_IAS_TRP)
  ##  List out all the missing dates
  sql_adobe = """
        SELECT
        DayInBetween AS missingDate
        FROM dbo.GetAllDaysInBetween('2019-01-01', 
	----  Find the Max date in the table/view
	(SELECT MAX([Day])
        FROM [DM_1406_TRowePrice].[dbo].[DFID052226_DS999621_Email_Omniture_TRP_US_Extracted])
	) AS AllDaysInBetween
	----  END: Find the Max date in the table/view
        WHERE NOT EXISTS 
        (SELECT [Visits] FROM [DM_1406_TRowePrice].[dbo].[DFID052226_DS999621_Email_Omniture_TRP_US_Extracted] WHERE [Day] = AllDaysInBetween.DayInBetween)
         """
  print("Finding Missing data gaps in Table [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted] ...")
  then = time.time() # Time before the operations start
  Adobedf = pd.read_sql(sql_adobe, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  maxdateAdobe = pd.read_sql(maxsql_adobe, Connection.engine)
  print("Max date for Table [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]: ", maxdateAdobe.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds\n")
  return Adobedf



def getSizmekTable():
  """
  Function to pull the Sizmek table (DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted)
      - print out the max data from the table
      - is there any missing date from the table 
  """
  maxsql_sizmek ="""
        SELECT MAX([DeliveryDate])
        FROM [DM_1406_TRowePrice].[dbo].[DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]
        """

  ##  Connecting Sizmek Table (DS020301_Sizmek_Campaign_Report)
  ##  List out all the missing dates
  sql_sizmek = """
        SELECT
        DayInBetween AS missingDate
        FROM dbo.GetAllDaysInBetween('2019-01-01', 
	----  Find the Max date in the table/view
	(SELECT MAX([DeliveryDate])
        FROM [DM_1406_TRowePrice].[dbo].[DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted])
	) AS AllDaysInBetween
	----  END: Find the Max date in the table/view
        WHERE NOT EXISTS 
        (SELECT [AccountID] FROM [DM_1406_TRowePrice].[dbo].[DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted] WHERE [DeliveryDate] = AllDaysInBetween.DayInBetween)
         """
  print("Finding Missing data gaps in Table [DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted] ...")
  then = time.time() # Time before the operations start
  Sizmekdf = pd.read_sql(sql_sizmek, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  maxdateSizmek = pd.read_sql(maxsql_sizmek, Connection.engine)
  print("Max date for Table [DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]: ", maxdateSizmek.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds")
  return Sizmekdf


def exporting():
  pass



def main():
  
  Connection()
  getIASTable()
  print("printing getIASTable\n",getIASTable())
  getAdobeTable()
  print("printing getAdobeTable\n",getAdobeTable())
  getSizmekTable()
  print("printing getSizmekTable\n",getSizmekTable())
  
main()
