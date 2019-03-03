### Author:     Han Thu  	  ###
### Date:       March 02, 2019    ###
### Client:     Chevron (DM_1485,  10.2.186.181\SQLINS04,4723) ###
### Description:
### Comparing data for Chevron client from "Prod" server vs "UAT"  ###
###      - (Innovid)  [DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
###      - (Innovid)  [DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted]
###      - (Sizmek)   [DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
### 


#!/usr/bin/env python     ## Set interpreter used to be the one on your environment's $PATH
import pyodbc
import time
import os
import datetime
from datetime import date
import xlsxwriter

"""
Handle datetime to str and print out in date format
https://github.com/mkleehammer/pyodbc/issues/329

def handleDateToString(dateObj):
    return dateObj.strftime('%H:%M:%S.%f')
"""



def ConnectAzureProd():
      ## Declaring gloabl lists to store the data from Azure
      ## so that the result will be exported to Excel
      global listA1
      global listA2
      global listA3
      listA1 = []
      listA2 = []
      listA3 = []
      print ("Connecting 'Chevron' client on Azure")
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=sqlsv-wm-us-prod.database.windows.net;DATABASE=SQLDB_Chevron_US;UID=DASuser;PWD=Passw0rd')
            ## Creating cursors to pull data from Chevron clients ##
      cursor1 = cnxn.cursor()   ## date cursor for "DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted"
      cursor2 = cnxn.cursor()   ## date cursor for "DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted"
      cursor3 = cnxn.cursor()   ## date cursor for "DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted"

            ########  Table 1  ########
            #### Creating list for <DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted> table
      listA1.append('DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted')
            ## Getting max date
      cursor1.execute(""" 
                SELECT MAX([Day])
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            listA1.append(record[0])
            #print("Max date in DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor1.execute("""
                SELECT count(*)
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            listA1.append(record[0])
            #print("Total Rows: ",record[0])
      print("listA1: ",listA1)

            ########  Table 2  ########
            ####  Creating list for <DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted> table
      listA2.append('DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted')
            ## Getting total number of rows
      cursor2.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted]
      """)
      for record in cursor2:
            listA2.append(record[0])
            #print("Total Rows: ",record[0])
      print("listA2: ",listA2)

            ########  Table 3  ########
            #### Creating list for <DS020307_Sizmek_Device_Video_Report_Chevron_Extracted> table
      listA3.append('DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted')
            ## Getting max date
      cursor3.execute(""" 
                SELECT MAX([Date])
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            sep = ' '   ## create separator for converting smalldatetime to str
            listA3.append(str(record[0]).split(sep,1)[0])
            #print("Max date in DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor3.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            listA3.append(record[0])
            #print("Total Rows: ",record[0])
      print("listA3: ",listA3)




def ConnectPremise():
      ## Declaring gloabl lists to store the data from Premise
      ## so that the result will be exported to Excel
      global listP1
      global listP2
      global listP3
      listP1 = []
      listP2 = []
      listP3 = []
      print ("Connecting 'Chevron' client in Premise ...")
      cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.2.186.181\SQLINS04,4723;DATABASE=DM_1485_Chevron;UID=DASuser01;PWD=DASpassw0rd')
            ## Creating cursors to pull data from Chevron clients In Premise ##
      cursor1 = cnxn.cursor()   ## date cursor for "DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted"
      cursor2 = cnxn.cursor()   ## date cursor for "DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted"
      cursor3 = cnxn.cursor()   ## date cursor for "DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted"

            ########  Table 1  ########
            #### Creating list for <DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted> table
      listP1.append('DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted')
            ## Getting max date
      cursor1.execute(""" 
                SELECT MAX([Day])
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            listP1.append(record[0])
            #print("Max date in DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor1.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066573_DS999922_Email_Innovid_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor1:
            listP1.append(record[0])
            #print("Total Rows: ",record[0])
      print("listP1: ",listP1)

            ########  Table 2  ########
            ####  Creating list for <DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted> table
      listP2.append('DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted')
            ## Getting total number of rows
      cursor2.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066576_DS999923_Email_Innovid_Device_Metadata_Report_Chevron_Extracted]
      """)
      for record in cursor2:
            listP2.append(record[0])
            #print("Total Rows: ",record[0])
      print("listP2: ",listP2)

            ########  Table 3  ########
            #### Creating list for <DS020307_Sizmek_Device_Video_Report_Chevron_Extracted> table
      listP3.append('DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted')
            ## Getting max date
      cursor3.execute(""" 
                SELECT MAX([Date])
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            sep = ' '   ## create separator for converting smalldatetime to str
            listP3.append(str(record[0]).split(sep,1)[0])
            #print("Max date in DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted: ",record[0])
            ## Getting total number of rows
      cursor3.execute(""" 
                SELECT count(*)
                FROM [dbo].[DFID066577_DS020307_Sizmek_Device_Video_Report_Chevron_Extracted]
      """)
      for record in cursor3:
            listP3.append(record[0])
            #print("Total Rows: ",record[0])
      print("listP3: ",listP3)




def matching(list1, list2):
      """
      Function to check if the two lists have same data.
      Reference:
      https://www.quora.com/How-can-I-do-a-comparison-of-two-lists-in-Python-with-each-value
      """
      #return [i for i, j in zip(list1,list2) if i==j]
      for item in list1:
            for item1 in list2:
                  if item == item1:
                        return 1 ## match
                  else:
                        return 0


def exporting():
      """
      Exporting to Excel sheet from the data (finallist1)      
      """
      df1 = getAzureData()
      df2 = getPremData()
      # find elements in df1 that are not in df2
      df_1notin2 = df1[~(df1['DeliveryDate'].isin(df2['DeliveryDate'])&
                         df1['Final Impressions'].isin(df2['Final Impressions'])&
                          df1['Final Clicks'].isin(df2['Final Clicks']) &
                           df1['Final Spend'].isin(df2['Final Spend']) &
                            df1['Final Spend - Flight'].isin(df2['Final Spend - Flight']                   
                           ))].reset_index(drop=True)

      writer = pd.ExcelWriter('Chevron_QA.xlsx')
      df1.to_excel(writer,'AzureData')
      df2.to_excel(writer,'PremData')
      df_1notin2.to_excel(writer,'Difference')
      writer.save()
      
      
      
def testing(mylist):
      """
      Exporting to Excel sheet from the data (finallist1)
      Reference:
      https://xlsxwriter.readthedocs.io/tutorial02.html
      """
      # Workbook is created 
      wb = xlsxwriter.Workbook('Chevron_QA.xlsx') 
      sheet1 = wb.add_worksheet()
      # add_sheet is used to create sheet. 
      #sheet1 = wb.add_sheet('Summary') 
        
      sheet1.write(1, 0, 'ISBT DEHRADUN') 
      sheet1.write(2, 0, 'SHASTRADHARA') 
      sheet1.write(3, 0, 'CLEMEN TOWN') 
      sheet1.write(4, 0, 'RAJPUR ROAD') 
      sheet1.write(5, 0, 'CLOCK TOWER') 
      sheet1.write(0, 1, 'ISBT DEHRADUN') 
      sheet1.write(0, 2, 'SHASTRADHARA') 
      sheet1.write(0, 3, 'CLEMEN TOWN') 
      sheet1.write(0, 4, 'RAJPUR ROAD') 
      sheet1.write(0, 5, 'CLOCK TOWER') 

      wb.close()
      #wb.save('xlwt example.xls') 
      

def main():
      os.system('cls')  ## clear the screen windows
      ConnectAzureProd()

      
      """
      ConnectPremise()
      finallist1 = matching(listA1,listP1)
      if(finallist1 ==1):
            listA1.append('Matched')
      else:
            listA1.append('UnMatched')
            
      finallist2 = matching(listA2,listP2)
      if(finallist2 ==1):
            listA2.append('Matched')
      else:
            listA2.append('UnMatched')
      
      finallist3 = matching(listA2,listP2)
      if(finallist3 ==1):
            listA3.append('Matched')
      else:
            listA3.append('UnMatched')
      
      #print("before...")
      #print(listA1)
      #print(listA2)
      #print(listA3)

      if(len(listP1) == len(listA1)):
            finallist1.append('Matched')
      else:
            finallist1.append('UnMatched')
      if(len(finallist2) == len(listA2)):
            finallist2.append('Matched')
      else:
            finallist2.append('UnMatched')
      if(len(finallist3) == len(listA3)):
            finallist3.append('Matched')
      else:
            finallist3.append('UnMatched')


      testing(finallist1) ## Exporting finallist1

      for i in range(1,len(listA1)+1):
            firstlistname= 'listA'+str(i)
            secondlistname = 'listP'+str(i)
            finallist.append(matching(firstlistname , secondlistname))
      print('before exporting')
      """
      #exporting()


main()

