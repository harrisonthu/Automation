### Author: Han Thu  	  ###
### Date: April 23, 2018  ###

import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=10.2.186.148\SQLINS02,4721;DATABASE=DM_1406_TRowePrice;UID=HThu;PWD=-----')
cursor = cnxn.cursor()

cursor.execute("SELECT * FROM sys.tables")
tables = cursor.fetchall()
#cursor.execute("SELECT WORK_ORDER.TYPE,WORK_ORDER.STATUS, WORK_ORDER.BASE_ID, WORK_ORDER.LOT_ID FROM WORK_ORDER")

for row in cursor.columns(table='WORK_ORDER'):
    print(row.column_name)
    
    for field in row:
        print(field)

print(tables)
