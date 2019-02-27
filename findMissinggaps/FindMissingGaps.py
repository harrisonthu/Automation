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
import pyodbc
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
  print("Connected ", Connection.Database, "!\n")


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
  #print("Finding Missing data gaps in Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted] ...")
  then = time.time() # Time before the operations start
  getIASTable.IASdf = pd.read_sql(sql, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  getIASTable.maxdateIAS = pd.read_sql(maxsql, Connection.engine)
  #print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", maxdateIAS.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds\n")
  return getIASTable.IASdf


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
  #print("Finding Missing data gaps in Table [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted] ...")
  then = time.time() # Time before the operations start
  getAdobeTable.Adobedf = pd.read_sql(sql_adobe, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  getAdobeTable.maxdateAdobe = pd.read_sql(maxsql_adobe, Connection.engine)
  #print("Max date for Table [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]: ", maxdateAdobe.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds\n")
  return getAdobeTable.Adobedf



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
  #print("Finding Missing data gaps in Table [DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted] ...")
  then = time.time() # Time before the operations start
  getSizmekTable.Sizmekdf = pd.read_sql(sql_sizmek, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  getSizmekTable.maxdateSizmek = pd.read_sql(maxsql_sizmek, Connection.engine)
  #print("Max date for Table [DFID061542_DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]: ", maxdateSizmek.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds")
  return getSizmekTable.Sizmekdf



def testingtable():
  """
  TESTING TABLE FOR this script !
  """
  
  maxsql = """
        SELECT MAX([visitDate])
        FROM [DM_1406_TRowePrice].[dbo].[Dummy_table__testing_data_missing_han]
        """

  sql = """
        SELECT
        DayInBetween AS missingDate
        FROM dbo.GetAllDaysInBetween('2019-01-01', 
	----  Find the Max date in the table/view
	(SELECT MAX([visitDate])
        FROM [DM_1406_TRowePrice].[dbo].[Dummy_table__testing_data_missing_han])
	) AS AllDaysInBetween
	----  END: Find the Max date in the table/view
        WHERE NOT EXISTS 
        (SELECT [visits] FROM [DM_1406_TRowePrice].[dbo].[Dummy_table__testing_data_missing_han] WHERE [visitDate] = AllDaysInBetween.DayInBetween)
        """
  #print("Finding Missing data gaps in Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted] ...")
  then = time.time() # Time before the operations start
  testingtable.Testingdf = pd.read_sql(sql, Connection.engine)  # store data frame type of the result
  now = time.time()  # Time after it finished
  testingtable.maxdateTesting = pd.read_sql(maxsql, Connection.engine)
  print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", testingtable.maxdateTesting.iloc[0,0])
  print("Finished finding missing data gaps. It took: ",int(now-then), " seconds\n")
  return testingtable.Testingdf




def main():
  Connection()
  getIASTable()
  #print("here is the IAS table printing", getIASTable())
  print("Finding missing data in IAS Table (DS999622_FTP_IAS_TRP) ...")
  if (getIASTable().empty):
    print("IAS Table does not have any missing data !")
    print("Max date for Table [DFID052284_DS999622_FTP_IAS_TRP_Extracted]: ", getIASTable.maxdateIAS.iloc[0,0])
    print("\n")
  else:
    print("IAS Table HAS missing data ! \n")
    print("Here is the missing date: \n",getIASTable.IASdf)
    
  print("Finding missing data in Adobe Table (DS999621_Email_Omniture_TRP) ...")
  getAdobeTable()
  #print("here is the Adobe table printing", getAdobeTable())
  if (getAdobeTable().empty):
    print("Adobe Table does not have any missing data !")
    print("Max date for Table [DFID052226_DS999621_Email_Omniture_TRP_US_Extracted]: ", getAdobeTable.maxdateAdobe.iloc[0,0])
    print("\n")
  else:
    print("Adobe Table HAS missing data ! \n")
    print("Here is the missing date: \n",getAdobeTable.Adobedf)

  print("Finding mising data in Sizmek Table (DS020301_Sizmek_Campaign_Report) ...")
  getSizmekTable()
  if (getSizmekTable().empty):
    print("Sizmek Table does not have any missing data !")
    print("Max date for Table [DS020301_Sizmek_Campaign_Report_TRowePrice_Extracted]: ", getSizmekTable.maxdateSizmek.loc[0,:].to_string())
    print("\n")
  else:
    print("Sizmek Table HAS missing data ! \n")
    print("Here is the missing date: \n",getSizmekTable.Sizmekdf)
  #testingtable()
  #if (testingtable().empty):
  #  print("TESTING Table does not have any missing data !\n")
  #else:
  #  print("TESTING Table HAS missing data ! \n")
  #  print("here is the missing date: \n",testingtable.Testingdf)

  os.system("pause")
  input("Press Enter to terminate the program: ")





main()













