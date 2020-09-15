#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 17:37:28 2020

@author: jaswithareddy

Encrypt and Decrypt text using Hill Cipher.
"""

import sys
import numpy as np

def encrypt():
    inp_key=input("Enter Key: ").upper()
    plaintxt = input("Enter Plain Text: ").upper()
    plaintxt = plaintxt.replace(" ", "")
    len_chk = 0
    if len(plaintxt) % 2 != 0:
        plaintxt += "0"
        len_chk = 1
    row = 2
    col = int(len(plaintxt)/2)
    plaintxt2d = np.zeros((row, col), dtype=int)
    
    itr0 = 0
    itr1 = 0
    for i in range(len(plaintxt)):
        if i % 2 == 0:
            plaintxt2d[0][itr0] = int(ord(plaintxt[i])-65)
            itr0 += 1
        else:
            plaintxt2d[1][itr1] = int(ord(plaintxt[i])-65)
            itr1 += 1

    key = " "
    for i in inp_key:
        key += i
    key = key.replace(" ", "").upper()
    key2d = np.zeros((2, 2), dtype=int)
    itr2 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr2])-65
            itr2 += 1
    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue

    if mul_inv == -1:
        print("Invalid key")
        sys.exit()
        
    cipher = ""
    itr_count = int(len(plaintxt)/2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = plaintxt2d[0][i] * key2d[0][0] + plaintxt2d[1][i] * key2d[0][1]
            cipher += chr((temp1 % 26) + 65)
            temp2 = plaintxt2d[0][i] * key2d[1][0] + plaintxt2d[1][i] * key2d[1][1]
            cipher += chr((temp2 % 26) + 65)
    else:
        for i in range(itr_count-1):
            temp1 = plaintxt2d[0][i] * key2d[0][0] + plaintxt2d[1][i] * key2d[0][1]
            cipher += chr((temp1 % 26) + 65)
            temp2 = plaintxt2d[0][i] * key2d[1][0] + plaintxt2d[1][i] * key2d[1][1]
            cipher += chr((temp2 % 26) + 65)
            
    print("Cipher Text: {}\n".format(cipher))


def decrypt():
    inp_key = input("Enter Key: ").upper()
    ciphertxt = input("Enter Cipher Text: ").upper()
    ciphertxt = ciphertxt.replace(" ", "")
    len_chk = 0
    if len(ciphertxt) % 2 != 0:
        ciphertxt += "0"
        len_chk = 1
    row = 2
    col = int(len(ciphertxt) / 2)
    ciphertxt2d = np.zeros((row, col), dtype=int)
    
    itr0 = 0
    itr1 = 0
    for i in range(len(ciphertxt)):
        if i % 2 == 0:
            ciphertxt2d[0][itr0] = int(ord(ciphertxt[i]) - 65)
            itr0 += 1
        else:
            ciphertxt2d[1][itr1] = int(ord(ciphertxt[i]) - 65)
            itr1 += 1

    key = " "
    for i in inp_key:
        key += i
    key = key.replace(" ", "").upper()
    key2d = np.zeros((2, 2), dtype=int)
    itr2 = 0
    for i in range(2):
        for j in range(2):
            key2d[i][j] = ord(key[itr2]) - 65
            itr2 += 1

    deter = key2d[0][0] * key2d[1][1] - key2d[0][1] * key2d[1][0]
    deter = deter % 26
    mul_inv = -1
    for i in range(26):
        temp_inv = deter * i
        if temp_inv % 26 == 1:
            mul_inv = i
            break
        else:
            continue
    key2d[0][0], key2d[1][1] = key2d[1][1], key2d[0][0]
    key2d[0][1] *= -1
    key2d[1][0] *= -1
    key2d[0][1] = key2d[0][1] % 26
    key2d[1][0] = key2d[1][0] % 26

    for i in range(2):
        for j in range(2):
            key2d[i][j] *= mul_inv
            
    for i in range(2):
        for j in range(2):
            key2d[i][j] = key2d[i][j] % 26

    plaintext = ""
    itr_count = int(len(ciphertxt) / 2)
    if len_chk == 0:
        for i in range(itr_count):
            temp1 = ciphertxt2d[0][i] * key2d[0][0] + ciphertxt2d[1][i] * key2d[0][1]
            plaintext += chr((temp1 % 26) + 65)
            temp2 = ciphertxt2d[0][i] * key2d[1][0] + ciphertxt2d[1][i] * key2d[1][1]
            plaintext += chr((temp2 % 26) + 65)
    else:
        for i in range(itr_count - 1):
            temp1 = ciphertxt2d[0][i] * key2d[0][0] + ciphertxt2d[1][i] * key2d[0][1]
            plaintext += chr((temp1 % 26) + 65)
            temp2 = ciphertxt2d[0][i] * key2d[1][0] + ciphertxt2d[1][i] * key2d[1][1]
            plaintext += chr((temp2 % 26) + 65)

    print("Plain Text: {}\n".format(plaintext))
    
if __name__=="__main__":
    while True:
        print("Enter:\n(1) to encrypt\n(2) to decrypt\n(3)to exit")
        n=int(input())
        if n==1:
            encrypt()
        elif n==2:
            decrypt()
        elif n==3:
            break
