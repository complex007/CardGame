#!/usr/bin/env python
#-*-encoding:utf-8 -*-


b=[x for x in range(100,1000)]


def decision(a):
    c=int(a/100)
    d=int((a-int(a/100)*100)/10)
    e=a%10
    if c**3+d**3+e**3==a:    
       return True

print filter(decision,b )