#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 11:58:32 2020

@author: jaswithareddy
"""

file_in=open("two.txt","r")
key=4
list_in=[]
for i in file_in.read():
    if i=='\n':
        break
    list_in.append(ord(i))
list_out=[]
for i in list_in:
    if (i+key)>ord('z'):
        list_out.append(chr((i+key)-26))
    else:
        list_out.append(chr(i+key))
for i in list_out:
    print(i,end='')
file_in.close()