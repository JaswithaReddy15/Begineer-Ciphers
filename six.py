#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 17:41:13 2020

@author: jaswithareddy

Create a key matrix for Playfair Cipher.
"""

alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
key=input("Enter Key: ")
m=[]

for e in key.upper():
    if e not in m:
        m.append(e)        
for e in alphabet:
    if e not in m:
        m.append(e)

key_matrix=[m[0:5],m[5:10],m[10:15],m[15:20],m[20:25]]

print("\nPlayfair Cipher Key Matrix:")
for i in key_matrix:
    for ele in i:
        print(ele,end=' ')
    print()
