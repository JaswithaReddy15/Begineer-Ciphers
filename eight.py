#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 20:38:57 2020

@author: jaswithareddy

Decrypt a cipher text using PlayFair Cipher.
"""
    
def locindex(c): 
    loc=[]
    if c=='J':
        c='I'
    for i ,j in enumerate(final_kmatrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def decrypt():  
    msg=input("ENTER CIPHER TEXT: ")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=[]
        loc=locindex(msg[i])
        loc1=[]
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(final_kmatrix[(loc[0]-1)%5][loc[1]],final_kmatrix[(loc1[0]-1)%5][loc1[1]]),end='')
        elif loc[0]==loc1[0]:
            print("{}{}".format(final_kmatrix[loc[0]][(loc[1]-1)%5],final_kmatrix[loc1[0]][(loc1[1]-1)%5]),end='')  
        else:
            print("{}{}".format(final_kmatrix[loc[0]][loc1[1]],final_kmatrix[loc1[0]][loc[1]]),end='')    
        i=i+2        
                            

if __name__=="__main__":
    key="SRMAPUNIVERSITY"
    key_matrix=[]
    for i in key: 
        if i not in key_matrix:
            if i=='J':
                key_matrix.append('I')
            else:
                key_matrix.append(i)
    flag=0
    for i in range(ord('A'),ord('Z')+1): 
        if chr(i) not in key_matrix:
            if i==ord('I') and 'J' not in key_matrix:
                key_matrix.append("I")
                flag=1
            elif flag==0 and i==ord('I') or i==ord('J'):
                pass   
            else:
                key_matrix.append(chr(i))
    k=0
    final_kmatrix=[[0 for i in range(5)] for j in range(5)]
    for i in range(0,5): 
        for j in range(0,5):
            final_kmatrix[i][j]=key_matrix[k]
            k+=1
    decrypt()
