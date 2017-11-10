import os, re
import glob
import csv
import sys
#import xlsxwriter


class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data):
        current = self.head
        previous = None
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())







##show current file directory
#myfilepath = os.getcwd()
#print(os.path.abspath(myfilepath))

## list out all of the txt files in the current directory
#arr = os.listdir()
#print("arr",arr)

#filepath = tab


null_str_list = ["N/A", "NULL", "N/A (Will be NULL"]



def readFile(filename):
    filehandle = open(filename)
    print(filehandle.read())
    filehandle.close()



#def returncolname():
fileDir = os.path.dirname(os.path.realpath('__file__'))
print("fileDir:",fileDir)
#For accessing the file in the same folder
filename = 'tab-separated-values.txt'
#print(readFile(filename))
#For accessing the file in a folder contained in the current folder
filename = os.path.join(fileDir, 'tab-separated-values.txt')
documents = open(filename, "r").readlines()

with open(filename) as f:
    content = f.readlines()
    content = [x.strip().split("\t") for x in content]
    #print("content:[0]   ",content[0]) 
    #print("")
    #print("content:[1]   ",content[1])
    

han_dic = dict(zip(content[0], content[1]))
templist = []

    
for key,value in han_dic.items():
    if value in null_str_list:
        aa = ",NULL as ["+ value+ "] as ["+ key,"]"
        templist.append(aa)
    else:
        cc = ","+value+ " as ["+key+"]"
        templist.append(cc)

for i in templist:
    print(i)


sorted(templist, key=lambda x: han_dict[key])



"""     
###  Printing ALL keys and values in dictionary
for key, value in han_dic.items():
    #print(key, '  ====>  ', value)
    for substr in value:
        if value in null_str_list:
            print(",NULL as [", value, "] as [", key,"]")
        else:
            print(",",value, " as [",key,"]")
        break


        
"""            




    
"""
for i in range(arr):
    with open(arr[4]) as input:
        zip(*(line.strip().split('\t') for line in input)


print('\n')
print(arr[4])
with open(arr[4], 'r') as f:
    hanfile = [x.strip().split('\t') for x in f]

print(hanfile)

print(sys.path[0])
lol = list(csv.reader(open(arr[4],'rb'),delimiter = '\t'))

#print(lol)


pattern = re.compile('word1(.*?)word3', flags=re.S)
for file in glob.glob('*.txt'):
    with open(file) as fp:
        for result in pattern.findall(fp.read()):
            print(result)

filename = open("tab-separated-values.txt", "r")
print("filename: ",filename)
for i in filename:
    print(i)

#lines = filename.readline()
lines = filename.read().split(',')
print(lines)
#print(sys.path[0])
#lol = list(csv.reader(open(arr[4],'rb'),delimiter = '\t'))


script_dir = os.path.dirname(__file__)
print(script_dir)
rel_path = " \tab-separated-values.txt"
abs_file_path = os.path.join(script_dir, rel_path)
print(abs_file_path)
"""






"""
haninput = str(readFile(filename))
f = open(filename)
print(f)
lines = f.readlines()
print(type(lines))
#output = lines.split("\t")
#print("readfile: ",readFile(filename))

hanlist = []
with open(filename) as f:
    for line in f:
        hanlist.append(line)

#print("line: ", line)
data = [word.split('\t','\n') for word in hanlist] 
print("data:" ,data)
"""


"""
with open('data.txt','r') as f:    
    lines = f.readlines()[1:]
    for line in lines:
        elements = line.strip().split("\t")
        print elements, len(elements)
"""





"""
def main():
    user_input = input("Do you want to convert to float <1> (or) return column name <2>??")
    if(user_input == '1'):
        print("To be continued")
    elif(user_input == '2'):
        returncolname()
    else:
        print("Sorry. I can't help bro !")
        

main()
"""     
        


