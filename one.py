#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:11:38 2020

@author: jaswithareddy
"""

file_in=open("one.txt","r")
print("Word: ",file_in.read())
file_in.close()

file_in=open("one.txt","r")
count=0
list_ASCII=[]
for i in file_in.read():
    if i=='\n':
        break
    count+=1
    list_ASCII.append(ord(i))
print("Character Count: ",count)
print("ASCII Values: ",list_ASCII)
file_in.close()