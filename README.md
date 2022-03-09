# Project_py
=================================================================================================================
import csv
import os
from wsgiref import headers


#Creating a class named project
class Project:
    def __init__(self,name):
        self.name=name
    #Creating a function named "func"
    def func(self):
        #creating a empty dictionary
        dic={}

        #opening a file
        f=open(self.name,"r")
        #reading lines in csv file
        lines=f.readlines()
        #reading the first line in a2.csv lines
        header=lines[:1]
        # Converting string in to a list
        head=header[0].strip()
        head=head.split(",")
        #reading the remaining lines in a2.csv lines

        rows=lines[1:]

        # reading each line in rows
        for row in rows:
            row=row.strip()
            values=row.split(" ")
            values=values[0].split(",")
            i=0
            # appending values to respective key in dictionary
            for val in values:
                dic.setdefault(head[i],[])
                dic[head[i]].append(val)
                i+=1
        return dic
    # printing the dictionary
    # print(dic)

Pro=Project("a2.csv")
Pro1=Project("a3.csv")
print(Pro1.func())
print(Pro.func())

===================================================================================

import pandasql as ps
import pandas as pd
 
 
#converting the data in dictionary into table format 
def func1(val):
    new = pd.DataFrame.from_dict(val)
    return new

v1=func1(Pro.func())
v2=func1(Pro1.func())

print(ps.sqldf("select * from v1"))

============================================================================================================================
