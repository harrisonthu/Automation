import pandas as pd
from sqlalchemy import create_engine

def getAzureData():
  # Parameters
  ServerName = "wmdata-us.database.windows.net"
  Database = "WM-NA-HBS"
  UserPwd = "DASuser:Passw0rd"
  Driver = "driver=SQL Server Native Client 11.0"

  # Create the connection
  print('Connecting ' + Database + ' Database ...')
  engine = create_engine('mssql+pyodbc://' + UserPwd + '@' + ServerName + '/' + Database + "?" + Driver)
  ##  Connecting Azure HBS server
  ##  for accessing Ad_Server_Prisma Table for 
  sql = """
    SELECT [DeliveryDate]
   ,SUM([Final Impressions]) as [Final Impressions]
   ,SUM([Final Clicks]) as [Final Clicks]
   ,SUM([Final Spend]) as [Final Spend]
   ,SUM([Final Spend - Flight]) as [Final Spend - Flight]
   from [dbo].[Ad_Server_Prisma]
   Group by [DeliveryDate]
   order by [DeliveryDate]
        """
  print("Connected " + Database)
  df = pd.read_sql(sql, engine)
  return df


def getPremData():
  # Parameters
  ServerName = "10.2.186.148\SQLINS02,4721"
  Database = "DM_913_HBSUSA"
  UserPwd = "DASuser01:DASpassw0rd"
  Driver = "driver=SQL Server Native Client 11.0"

  # Create the connection
  print('Connecting ' + Database + ' Database ...')
  engine = create_engine('mssql+pyodbc://' + UserPwd + '@' + ServerName + '/' + Database + "?" + Driver)
  ##  Connecting In Premise HBS server
  ##  for accessing Ad_Server_Prisma Table for 
  sql = """
    SELECT [DeliveryDate]
   ,SUM([Final Impressions]) as [Final Impressions]
   ,SUM([Final Clicks]) as [Final Clicks]
   ,SUM([Final Spend]) as [Final Spend]
   ,SUM([Final Spend - Flight]) as [Final Spend - Flight]
   FROM [DM_913_HBSUSA].[dbo].[Ad_Server_Prisma]
   Group by [DeliveryDate]
   order by [DeliveryDate]
        """
  print("Connected "+ Database)
  df = pd.read_sql(sql, engine)
  return df



def exportData():
  data = getData()
  export = data.to_csv('foo.csv')


def main():
  df1 = getAzureData()
  df2 = getPremData()
  print(df1.equals(df2))
  #print(df2)

main()



