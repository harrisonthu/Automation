import os, re
import glob
import csv
import sys


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


head = []
table = []
first = True

null_str_list = ["N/A", "NULL", "N/A (Will be NULL)"]

for i in open('tab-separated-values.txt'):
    i = i.strip()
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
            aa = ",NULL as ["+ value+ "] as ["+ key,"]"
            templist.append(aa)
        else:
            cc = ","+value+ " as ["+key+"]"
            templist.append(cc)
            
for i in templist:
    print(i)
