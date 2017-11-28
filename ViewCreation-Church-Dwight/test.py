import os
import sys


null_str_list = ["N/A", "NULL", "N/A (Will be NULL)"]

def returncolname():
    head = []
    table = []
    first = True
    ## Read the file (txt)
    for i in open('tab-separated-values.txt'):
        i = i.strip()  ## remove trailing
        if first:
            head = i.split('\t')
            first = False
        else:
            table = table + [i.split('\t')]

    templist = []

    for row in table:
        for i in range(len(head)):
            value = row[i]
            key = head[i]
            if value in null_str_list:
                #aa = ',NULL as ['+ value+ '] as ['+ key,']'
                aa = ',NULL as ['+ key,']'
                #templist.append(aa)
                templist.append(" ".join(aa))
            else:
                myvalue = ",["+value+ "] as ["+key+"]"
                templist.append(myvalue)              
    for i in templist:
        print(i)


def convfloatcolname():
    head = []
    table = []
    first = True
    ## Read the file (txt)
    for i in open('FLOAT-to-be-converted.txt'):
        i = i.strip()  ## remove trailing
        if first:
            head = i.split('\t')
            first = False
        else:
            table = table + [i.split('\t')]

    templist = []
    
    


    for row in table:
        for i in range(len(head)):
            key = head[i]
            ##print("key:::::::::", key)
            value = row[i]
            ## if item in txt file contains NULL
            if value in null_str_list:
                ## print out with Float Null format
                hanfloat = ',CONVERT(FLOAT,NULL) as [', key+']'
                templist.append(" ".join(hanfloat))
            ## if item in txt does NOT contains NULL
            else:
                cc = ", ["+value+ "] as ["+key+"]"
                templist.append(cc)              
    for i in templist:
        print(i)

 ###  input:::  Child Any Promo Dollars Chg vs. Yago
 ###  Final:::  ,convert(float,NULL) as [Child Any Promo Dollars Chg vs. Yago]



def main():
    user_input = input("Do you want to convert to float <1> (or) return column name <2>?? ")
    if(user_input == '1'):
        convfloatcolname()
    elif(user_input == '2'):
        returncolname()
    else:
        print("Sorry. I can't help !")
        

main()

