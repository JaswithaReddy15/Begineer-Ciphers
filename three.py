#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 12:36:01 2020

@author: jaswithareddy
"""

file_in=open("three.txt",'r')
list_in=[]
for i in file_in.read():
    if i=='\n':
        break
    list_in.append(ord(i))
list_out=[]
for key in range(1,26):
    print(key,end=' ')
    for i in list_in:
        if i==ord(' '):
            list_out.append(" ")
        elif (i+key)>ord('Z'):
            list_out.append(chr((i+key)-26))
        else:
            list_out.append(chr(i+key))
    for i in list_out:
        print(i,end='')
    print()
    list_out.clear()
file_in.close()