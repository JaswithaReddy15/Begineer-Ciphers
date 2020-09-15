#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 21:58:02 2020

@author: jaswithareddy
"""

def decrypt(message, keyword):
  matrix = createDecrMatrix(getKeywordSequence(keyword), message)

  plaintext = "";
  for r in range(len(matrix)):
    for c in range (len(matrix[r])):
      plaintext += matrix[r][c]
  return plaintext


def createDecrMatrix(keywordSequence, message):
  width = len(keywordSequence)
  height = int(len(message) / width)
  if height * width < len(message):
    height += 1

  matrix = createEmptyMatrix(width, height, len(message))

  pos = 0
  for num in range(len(keywordSequence)):
    column = keywordSequence.index(num+1)

    r = 0
    while (r < len(matrix)) and (len(matrix[r]) > column):
      matrix[r][column] = message[pos]
      r += 1
      pos += 1

  return matrix


def createEmptyMatrix(width, height, length):
  matrix = []
  totalAdded = 0
  for r in range(height):
    matrix.append([])
    for c in range(width):
      if totalAdded >= length:
        return matrix
      matrix[r].append('')
      totalAdded += 1
  return matrix


def getKeywordSequence(keyword):
  sequence = []
  for pos, ch in enumerate(keyword):
    previousLetters = keyword[:pos]
    newNumber = 1
    for previousPos, previousCh in enumerate(previousLetters):
      if previousCh > ch:
        sequence[previousPos] += 1
      else:
        newNumber += 1
    sequence.append(newNumber)
  return sequence

if __name__=="__main__":
    keyword=input("Enter Key: ")
    message=input("Enter Cipher Text: ")
    plain=decrypt(message,keyword)
    print("Plain Text: ",plain)