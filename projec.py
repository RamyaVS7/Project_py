import csv
import os
from wsgiref import headers

#creating a empty dictionary
dic={}

#opening a file
f=open("a2.csv","r")
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

# printing the dictionary
print(dic)

# print(type(head))


#creating a new dictionary
dic1={}
# opening a3.csv file and storing it in f1
f1=open("a3.csv","r")

#reading the lines in f1
lines1=f1.readlines()
header1=lines1[:1]
head1=header1[0].strip()
head1=head1.split(",")
print(head1)
rows1=lines1[1:]
j=0
for row1 in rows1:
    row1=row1.strip()
    values1=row1.split(" ")
    values1=values1[0].split(",")
    i=0
    for val in values1:
        dic1.setdefault(head1[i],[])
        dic1[head1[i]].append(val)
        i+=1

print(dic1)


import pandas as pd
 
 
data1 = dic1
data=dic
new = pd.DataFrame.from_dict(data)
new1 = pd.DataFrame.from_dict(data1)

 
print(new)
print(new1)


import pandasql as ps

print(ps.sqldf("select * from new"))