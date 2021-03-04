# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:55:22 2019

@author: User
"""
strr = ",[>+>+<<-]>[>[>+>+<<-]>>[<<+>>-]<<<-]>[>[>+>+<<-]>>[<<+>>-]<<<-]>><[>++<-]>+++++"
strr0 = "++[>+++[>+<-]<-]"
strr4 = ",[->+>+<<]>>[-<<+>>]<<>[<[->>+>+<<<]>>>[-<<<+>>>]<<-]>."
strr1 = "+++[>+++<-]>>+++"
strr2 = "++++++++++++++++++++[>++++>+++++>++++++>++++>+++++>+++++>+++++>+++++>++++>+++++<<<<<<<<<<-]>+++.>++++++++++++++++++.>+.>+++++++++++++++++.>++++++++++++++++.>+++++++++++.>+++++++++++++++.>++++++++.>+++++++++++++++++.>++++++++++++++++++.>.++++++++++++++++++++[>++++>+++++>++++++>++++>+++++>+++++>+++++>+++++>++++>+++++<<<<<<<<<<-]>++++.>+++++++++++++++.>+.>+++++++++++++++++++++++++++++.>--.>---.>++++++++."
global i
i = 0

tmparray = [0]
j = 0
def plusOne ():
    tmparray[j] = tmparray[j] + 1
def minusOne():
    tmparray[j] = tmparray[j] - 1
def plusPlace():
    tmparray.append(0)
    global j
    j += 1
def minusPlace():
    global j
    j -= 1
def Pass():
    pass
def Print():
    print(chr(tmparray[j]))

def Input():
    tmparray[j] = int(input("something"))
def cycle4(): #первый вариант
    varj = j 
    vari = i + 1
    while(tmparray[varj] > 1):
        if (strr[vari] == "]"):
            vari = i + 1
        commands[strr[vari]]();
        vari += 1
def cycle3(): #второй вариант
    global i
    varj = j 
    vari = i + 1
    while(True):
        if (strr[vari] == "]"):
            checkpoint = vari
            vari = i + 1
        elif (tmparray[varj] == 0):
            i = checkpoint + 1
            break
        commands[strr[vari]]();
        vari += 1

def cycle1(): #третий вариант
    print("cycle")
    global i
    varj = j 
    saveI = i + 1
    i = i + 1
    while(True):
        if (strr[i] == "]"):
            checkpoint = i + 1
            i = saveI
        elif (tmparray[varj] == 0):
            i = checkpoint
            return
        commands[strr[i]]();
        i += 1
    
def cycle(): #final
    global i
    varj = j 
    saveI = i + 1
    i = saveI
    while(True):
        if (strr[i] == "]") and (tmparray[varj] == 0):          
            #i += 1
            return
        elif (strr[i] == "]"):
            i = saveI
        else:
            commands[strr[i]]();
            i += 1
        
        
commands = {">": plusPlace,
            "<": minusPlace,
            "+": plusOne,
            "-": minusOne,
            ".": Print,
            ",": Input,
            "[": cycle,
            "]": Pass}
            

   
        
while (i < len(strr)):
   
    commands[strr[i]]();
    i += 1
tmpvar = len(tmparray) - 1
while(tmparray[tmpvar] == 0):
    tmparray.pop(tmpvar)
    tmpvar -= 1
print(tmparray) 



