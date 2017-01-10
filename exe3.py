#!/usr/bin/env python
#-*-encoding:utf-8 -*-
import pprint
f=open("dat_files.txt","r")
files=f.readlines()
f.close()
dict1={}
for i in files:
    item=i.split("/")[-1][:-1]
    if not (item in dict1.keys()) :
        dict1.update({item:i[:-1]})
pprint.pprint(dict1)
    


