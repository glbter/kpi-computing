# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 10:02:07 2019

@author: User
"""
import numpy as np
a = np.array([[0,1,0,0,1],
              [1,1,0,1,0],
              [1,0,1,0,1],
              [0,1,1,1,1],
              [1,0,0,0,1]])

b  = np.array([[0,1,0,0,1],
               [1,1,0,1,0],
               [1,0,1,0,1],
               [0,1,1,1,1],
               [1,0,0,0,1]])

def reflexive(matrix):
    tmp = 0
    for i in range(len(matrix)):
        if matrix[i][i] == 1:
            tmp += 1
    if tmp == len(matrix):
        return "matrix is reflexive"
    elif tmp == 0:
        return "matrix is antireflexive"
    else:
        return "matrix is not reflexive"
    
def symetrical(matrix):
    tmp = 0
    z=0
    anti = 0
    for i in range(z, len(matrix)):
        for j in range(z, len(matrix)):
            if i == j:
                continue
            if matrix[i][j] == matrix[j][i]:
                tmp += 1
                if matrix[i][j] == 0 and i>j:
                    anti += 1
        z += 1
    check = (len(matrix)**2 - len(matrix) )/2
    if tmp == check:
        return "matrix is symetrical"
    elif tmp == 0:
        return "matrix is asymetrical"
    if anti == check/2: #введены правки, что бы проверять лишь нижнюю часть
        return "matrix is antisymetircal"
    else:
        return "matrix is not symetrical"
            
        
def transitive(matrix):
    transit = 0
    antitransit = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] and matrix[j][k] and matrix[i][k] :
                    transit += 1
                elif matrix[i][j] and matrix[j][k] and not matrix[i][k] :
                    antitransit += 1
    if transit != 0 and antitransit == 0:
        return "matrix is transitive"
    elif transit == 0 and antitransit != 0:
        return "matrix is antitransitive"
    elif transit != 0 and antitransit != 0:
        return "matrix is not transitive"
                    
    return(transit)

def equivalent(matrix):
    if reflexive(matrix) == "matrix is reflexive" \
        and transitive(matrix) == "matrix is transitive" \
        and symetrical(matrix) == "matrix is symetrical":
        return "Yes"
    else:
        return "No"

def particalOrder(matrix):
    if reflexive(matrix) == "matrix is reflexive"\
        and transitive(matrix) == "matrix is transitive"\
        and symetrical(matrix) == "matrix is antisymetircal":
            return "Yes"
    else:
        return "No"
    


def reflexiveClosure(matrix):        
    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            matrix[i][i] = 1
            
def symetricalClosure(matrix):
    z=0
    for i in range(z, len(matrix)):
        for j in range(z, len(matrix)):
            if i == j:
                continue
            if matrix[i][j] == matrix[j][i]:
                continue
            else:
                if matrix[i][j] == 0:
                    matrix[i][j] = 1
                elif matrix[j][i] == 0:
                    matrix[j][i]
                    
def antisymetricalClosure(matrix):
    z=0
    for i in range(z, len(matrix)):
        for j in range(z, len(matrix)):
            if i == j:
                continue
            if i>j and matrix[i][j] != 0:
                matrix[i][j] = 0
    
def transitiveClosure(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] == 1 and matrix[j][k] == 1: 
                    matrix[i][k] = 1

def particularOrderClosure(matrix):
    if symetrical(matrix) != "matrix is antisymetrical" :
        antisymetricalClosure(a)
    if reflexive(matrix) != "matrix is reflexive":
        reflexiveClosure(a)
    if transitive(matrix) != "matrix is transitive":
        transitiveClosure(a)
def equivalenceClosure(matrix):
    if symetrical(matrix) != "matrix is symetrical" :
        symetricalClosure(a)
    if reflexive(matrix) != "matrix is reflexive":
        reflexiveClosure(a)
    if transitive(matrix) != "matrix is transitive":
        transitiveClosure(a) 
    
def power2(matrix):   
    array = np.dot(matrix,matrix)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j]>1:
                array[i][j] = 1
    return array
        
def power3(matrix): 
    array = np.dot(matrix,matrix)
    array = np.dot(array,matrix)
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j]>1:
                array[i][j] = 1
    return array

# =============================================================================
# print(symetrical(a))   
# print(transitive(a))
# print(reflexive(a))
# =============================================================================

# =============================================================================
# print(equivalent(b))                   
# print(particalOrder(b))  
# =============================================================================

# =============================================================================
# print(power2(a))
# print()
# print(power3(a))
# =============================================================================

# =============================================================================
# equivalenceClosure(a)
# antisymetricalClosure(a)
# print(a)
# =============================================================================
















