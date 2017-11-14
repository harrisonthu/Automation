import os
 ###  input:::  Child Any Promo Dollars Chg vs. Yago
 ###  Final:::  ,convert(float,NULL) as [Child Any Promo Dollars Chg vs. Yago]


"""
#def returncolname():
fileDir = os.path.dirname(os.path.realpath('__file__'))
print("fileDir:",fileDir)
#For accessing the file in the same folder
filename = 'FLOAT-to-be-converted.txt'
#print(readFile(filename))
#For accessing the file in a folder contained in the current folder
filename = os.path.join(fileDir, 'FLOAT-to-be-converted.txt')
documents = open(filename, "r").readlines()


## Read line in a file and put into the list content array
with open(filename) as f:
    content = f.readlines()
    content = [x.strip().split("\t") for x in content]
    print("content:[0]   ",content[0]) 
    print("")
    print("content:[1]   ",content[1])
"""



null_str_list = ["N/A", "NULL", "N/A (Will be NULL)"]

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
            value = row[i]
            key = head[i]
            ## if item in txt file contains NULL
            if value in null_str_list:
                ## print out with Float Null format
                hanfloat = ',CONVERT(FLOAT,NULL) as ['+ key,']'
                templist.append(",".join(hanfloat))
            ## if item in txt does NOT contains NULL
            else:
                cc = ","+value+ " as ["+key+"]"
                templist.append(cc)              
    for i in templist:
        print(i)


    
convfloatcolname()

