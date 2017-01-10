#!/usr/bin/env python
#-*-encoding:utf-8 -*-

list1 =[2, 31,2,52,1,52,1,23,4,6,88,4,45,27,54,43,745,23,68,345,2,6,45,8,8,7,5,334,2346,323]
# list1.sort( reverse=True)
# print list1

for x in range(len(list1)):
    if (x==len(list1)-1):
        continue
    for y in range(len(list1)):   
        if y<=x:
            continue   
        if list1[x]<list1[y]: 
            maxnum=list1[y]
            list1[y]=list1[x]
            list1[x]=maxnum 
print list1


            