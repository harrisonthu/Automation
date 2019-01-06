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
   WHERE [DeliveryDate] > '2018-01-01'
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
   WHERE [DeliveryDate] > '2018-01-01'
   Group by [DeliveryDate]
   order by [DeliveryDate]
        """
  print("Connected "+ Database)
  df = pd.read_sql(sql, engine)
  return df


def exporting():
  """
    Exporting the data(dataframe type) to excel(xlsx) format so that we can QA
    For Reference:  http://pbpython.com/excel-diff-pandas.html
  """
  dfA = getAzureData()
  dfP = getPremData()
  writer = pd.ExcelWriter('output.xlsx')
  dfA.to_excel(writer,'Sheet1')
  dfP.to_excel(writer,'Sheet2')
  writer.save()


def report_diff(x):
  """
   Define the diff function to show the changes in each field
   Reference:  http://pbpython.com/excel-diff-pandas.html
   
  """
  return x[0] if x[0] == x[1] else 'No'


def has_change(row):
  """
    We want to be able to easily tell which rows have changes
  """
  if "--->" in row.to_string():
    return "Y"
  else:
    return "N"

  
def compare_data():
  """
    Compare two data frames by creating a panel
    Apply the diff function
    flag all the changes
    Save the change to Excel but only include the columns we care about
  """
  df1 = getAzureData()
  df2 = getPremData()
  writer = pd.ExcelWriter('output.xlsx')
  df1.to_excel(writer,'AzureData')
  df2.to_excel(writer,'PremData')
  

  # Create a Pandas Excel writer using XlsxWriter as the engine.
  # Save the unformatted results
  writer_orig = pd.ExcelWriter('simple.xlsx', engine='xlsxwriter')
  df.to_excel(writer_orig, index=False, sheet_name='report')
  writer_orig.save()
    
  # Create a Pandas Excel writer using XlsxWriter as the engine.
  writer = pd.ExcelWriter('fancy.xlsx', engine='xlsxwriter')
  df.to_excel(writer, index=False, sheet_name='report')

  # Get access to the workbook and sheet
  workbook = writer.book
  worksheet = writer.sheets['report']
  worksheet.set_zoom(90)


def testing():
  df1 = getAzureData()
  df2 = getPremData()
  dictionary = {1:df1,2:df2}
  print('dictionary: ', dictionary)
  df=pd.concat(dictionary)
  df.drop_duplicates(keep=False)
  writer = pd.ExcelWriter('output.xlsx')
  df1.to_excel(writer,'AzureData')
  df2.to_excel(writer,'PremData')
  df.to_excel(writer,'Summary')
  writer.save()

  # Excel color format output
  # Reference: http://pbpython.com/improve-pandas-excel-output.html

def testing2():
  df1 = getAzureData()
  df2 = getPremData()
  mergedStuff= pd.merge(df1,df2, on =['DeliveryDate','Final Spend', 'Final Clicks', 'Final Impressions'], how= 'left')
  mergedStuff.head()
  writer = pd.ExcelWriter('output.xlsx')
  df1.to_excel(writer,'AzureData')
  df2.to_excel(writer,'PremData')
  mergedStuff.to_excel(writer,'Summary')
  writer.save()


def testing3():
  df1 = getAzureData()
  df2 = getPremData()
  df3 = pd.concat([df1,df2])
  df3 = df3.reset_index(drop=True)
  df_gpby = df3.groupby(list(df3.columns))
  idx = [x[0] for x in df3.gpby.groups.values() if len(x) ==1]
  df = df3.reindex(idx)
  writer = pd.ExcelWriter('output.xlsx')
  df1.to_excel(writer,'AzureData')
  df2.to_excel(writer,'PremData')
  df.to_excel(writer,'Summary')
  writer.save()

  
def diff_pd(df1, df2):
    """Identify differences between two pandas DataFrames"""
    assert (df1.columns == df2.columns).all(), \
        "DataFrame column names are different"
    if any(df1.dtypes != df2.dtypes):
        "Data Types are different, trying to convert"
        df2 = df2.astype(df1.dtypes)
    if df1.equals(df2):
        return None
    else:
        # need to account for np.nan != np.nan returning True
        diff_mask = (df1 != df2) & ~(df1.isnull() & df2.isnull())
        ne_stacked = diff_mask.stack()
        changed = ne_stacked[ne_stacked]
        changed.index.names = ['id', 'col']
        difference_locations = np.where(diff_mask)
        changed_from = df1.values[difference_locations]
        changed_to = df2.values[difference_locations]
        return pd.DataFrame({'from': changed_from, 'to': changed_to},
                            index=changed.index)

def testing4():
  df1 = getAzureData()
  df2 = getPremData()
  # find elements in df1 that are not in df2
  df_1notin2 = df1[~(df1['DeliveryDate'].isin(df2['DeliveryDate'])&
                     df1['Final Impressions'].isin(df2['Final Impressions'])&
                      df1['Final Clicks'].isin(df2['Final Clicks']) &
                       df1['Final Spend'].isin(df2['Final Spend']) &
                        df1['Final Spend - Flight'].isin(df2['Final Spend - Flight']                   
                       ))].reset_index(drop=True)

  writer = pd.ExcelWriter('output.xlsx')
  df1.to_excel(writer,'AzureData')
  df2.to_excel(writer,'PremData')
  df_1notin2.to_excel(writer,'Summary')
  writer.save()

def main():
  #df1 = getAzureData()
  #df2 = getPremData()
  #print(df1.equals(df2))
  #print(df2)
  #compare_data()
  testing4()



main()



