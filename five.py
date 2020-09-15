#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:32:28 2020

@author: jaswithareddy
"""

mapping={'A':'A','B':'N','C':'D','D':'R','E':'E','F':'W','G':'I','H':'C','I':'K','J':'S','K':'O','L':'H','M':'T','N':'B','O':'F','P':'G','Q':'J','R':'L','S':'M','T':'P','U':'Q','V':'U','W':'V','X':'X','Y':'Y','Z':'Z'}

file_in=open("five.txt",'r')
list_in=[]
for i in file_in.read():
    if i=='\n':
        break
    list_in.append(i)
list_out=[]
for i in list_in:
    list_out.append(mapping[i])
for j in list_out:
    print(j,end='')
file_in.close()
