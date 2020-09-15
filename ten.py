#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:37:39 2020

@author: jaswithareddy
"""

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

while(True):
    print("\n Enter:\n (1) to encypt\n (2) to decrypt\n (3) to exit")
    n=int(input())
    if n==1: #encrypt    
        key=input("Enter Key: ")
        list_key=[]
        for i in key:
            list_key.append(alphabet.index(i))
        plaintxt=input("Enter Plain Text: ")    
        list_plaintxt=[]
        for i in plaintxt:
            list_plaintxt.append(alphabet.index(i))    
        list_cipher=[]
        for x in range(0,len(plaintxt)):
            if list_key[x]+list_plaintxt[x]>25:
                add=list_key[x]+list_plaintxt[x]-26
            else:
                add=list_key[x]+list_plaintxt[x]
            list_cipher.append(alphabet[add])
        print("\nCipher Text:",end='')
        for i in list_cipher:
            print(i,end='')
        print()    
    elif n==2: #decrypt
        key=input("Enter Key: ")
        list_key=[]
        for i in key:
            list_key.append(alphabet.index(i))
        ciphertxt=input("Enter Cipher Text: ")    
        list_ciphertxt=[]
        for i in ciphertxt:
            list_ciphertxt.append(alphabet.index(i))
        list_plain=[]
        for x in range(0,len(ciphertxt)):
            if list_ciphertxt[x]-list_key[x]<0:
                sub=(list_ciphertxt[x]-list_key[x])+26
            else:
                sub=list_ciphertxt[x]-list_key[x]
            list_plain.append(alphabet[sub])
        print("\nPlain Text:",end='')
        for i in list_plain:
            print(i,end='')
        print()
    elif n==3:
        break
        