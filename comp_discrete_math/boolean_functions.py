# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 22:43:44 2019

@author: User
"""

import numpy as np
func = "11011111"

table = [[0, 0, 0],
          [0, 0, 1],
          [0, 1, 0],
          [0, 1, 1],
          [1, 0, 0],
          [1, 0, 1],
          [1, 1, 0],
          [1, 1, 1]]

def truthTable(func):
    tmptable = table
    tmp = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for i in range(len(func)):
        tmptable[i] = np.append(tmptable[i], int(func[i]))
    for i in range(len(tmptable)):
        tmp[i] = tmptable[i] 
    return tmp


def constantZero(func):
    res= "зберігає 0" if int(func[0]) == 0 else "не зберігає 0"
    return res

def constantOne(func):
    res= "зберігає 1" if int(func[7]) == 1 else "не зберігає 1"
    return res

def self_dual(func):
    res = "самодвоїста" if int(func[0]) != int(func[7]) else "не самодвоїста"
    return res

def linear(func):
    #polinomical coefficients
    a = int(func[0])     #000
    b = a ^ int(func[4]) #100
    c = a ^ int(func[2]) #010
    d = a ^ int(func[1]) #001
    e = a ^ b ^ c ^ int(func[6]) #110
    f = a ^ b ^ d ^ int(func[5]) #101
    g = a ^ c ^ d ^ int(func[3]) #011
    h = a ^ b ^ c ^ d ^ int(func[7]) #111
    if (e == 0) and (f == 0) and (g == 0) and (h == 0):
        return "лінійна"
    else :
        return "не лінійна"
 
def DNF(func):
    res = ""
    for i in range(len(func)):
        if func[i] == "1":
            res = res + "("
            for j in range(len(table[i])):
                
                if table[i][j] == 0 :
                    res = res + "¬"
                if j == 0:
                    res = res + "x ⋀ "
                elif j == 1:
                    res = res + "y ⋀ "
                elif j == 2:
                    res = res + "z ⋀ "
            res = res[0:len(res)-3]
            res = res + ") ⋁ "
    res = res[0:len(res)-2]
    return res     
   
def KNF(func):
    res = ""
    for i in range(len(func)):
        if func[i] == "0":
            res = res + "("
            for j in range(len(table[i])):
                
                if table[i][j] == 1 :
                    res = res + "¬"
                if j == 0:
                    res = res + "x ⋁ "
                elif j == 1:
                    res = res + "y ⋁ "
                elif j == 2:
                    res = res + "z ⋁ "
            res = res[0:len(res)-3]
            res = res + ") ⋀ "
    res = res[0:len(res)-2]
    return res  

print(truthTable(func))
print(constantZero(func))
print(constantOne(func))
print(self_dual(func))
print(linear(func))
print(DNF(func))
print()
print(KNF(func))














