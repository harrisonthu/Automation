import os
 ###  input:::  Child Any Promo Dollars Chg vs. Yago
 ###  Final:::  ,convert(float,NULL) as [Child Any Promo Dollars Chg vs. Yago]



#def returncolname():
fileDir = os.path.dirname(os.path.realpath('__file__'))
print("fileDir:",fileDir)
#For accessing the file in the same folder
filename = 'FLOAT-to-be-converted.txt'
#print(readFile(filename))
#For accessing the file in a folder contained in the current folder
filename = os.path.join(fileDir, 'FLOAT-to-be-converted.txt')
documents = open(filename, "r").readlines()


## Read line in a file and put into the list content 1 and content 2
with open(filename) as f:
    content = f.readlines()
    content = [x.strip().split("\t") for x in content]
    print("content:[0]   ",content[0]) 
    print("")
    print("content:[1]   ",content[1])
    


