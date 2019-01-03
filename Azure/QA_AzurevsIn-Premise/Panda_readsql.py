import pandas as pd
from sqlalchemy import create_engine

def getData():
  # Parameters
  ServerName = "wmdata-us.database.windows.net"
  Database = "WM-NA-HBS"
  UserPwd = "DASuser:Passw0rd"
  Driver = "driver=SQL Server Native Client 11.0"

  # Create the connection
  print('Connecting ' + Database + 'Database')
  engine = create_engine('mssql+pyodbc://' + UserPwd + '@' + ServerName + '/' + Database + "?" + Driver)
  ##  Ad_Server_Prisma
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
  print("connected")
  df = pd.read_sql(sql, engine)
  return df

df2 = getData()
print(df2)
