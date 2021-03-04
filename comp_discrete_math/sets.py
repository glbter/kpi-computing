# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 09:14:37 2019

@author: User
"""
univ = [1,2,3,4,5,6,7,8]
arr1 = str(input())
arr1 = arr1.split()
arr2 = str(input())
arr2 = arr2.split()
def Recast(arr):
    for i in range(0,len(arr)):
        arr[i] = int(arr[i])
    return arr

arr1 = Recast(arr1)
arr2 = Recast(arr2)

def Union(arr1, arr2):
    arr3 = []
    for elem in arr1:
        if elem not in arr3:
            arr3.append(elem)
    for elem in arr2:
        if elem not in arr3:
            arr3.append(elem)
    return arr3

def Intersection(arr1,arr2):
    arr3 = []
    for elem in arr1:
        if (elem in arr1) and (elem in arr2):
            arr3.append(elem)

    return arr3

def Difference(arr1,arr2):
    arr3 = []
    inter = Intersection(arr1,arr2)
    for elem in arr1:
        if elem not in inter:
            arr3.append(elem)
    return arr3

def SymetricalDifference(arr1, arr2):
    set1 = Difference(arr1, arr2)
    set2 = Difference(arr2, arr1)
    return Union(set1, set2)

def Complement(arr1, univ):
    return Difference(arr1, univ)

def CartesianProduct(arr1, arr2):
    res = []
    tmp = []
    for i in range (0,len(arr1)):
        for j in range (0, len(arr2)):
            tmp.append(arr1[i])
            tmp.append(arr2[j])
            res.append(tuple(tmp))
            tmp = []
    return res

def IsEqual (arr1, arr2):
    def Tmp(tmparr1, tmparr2):
        for elem in tmparr1:
            if not (elem in tmparr2):
                return False
        return True    
    return(Tmp(arr1, arr2) and Tmp(arr2, arr1))

def IsSubSet(Set, subSet):
    return IsEqual(Union(Set, subSet), Set) and IsEqual(Intersection(Set,subSet), subSet)
    
def BitRepr(Set, univ):
    res = []
    for elem in univ:
        if elem in Set:
            res.append(1)
        else:
            res.append(0)
    return res

def BitUnion (arr1, arr2, univ):
    Set = BitRepr(arr1, univ)
    Set2 = BitRepr(arr2, univ)
    res = []
    for i in range(0, len(univ)):
        if (Set[i] == 1) or (Set2[i] == 1):
            res.append(1)
        else:
            res.append(0)
    return res

def BitIntersection (arr1, arr2, univ):
    Set = BitRepr(arr1, univ)
    Set2 = BitRepr(arr2, univ)
    res = []
    for i in range(0, len(univ)):
        if (Set[i] == 1) and (Set2[i] == 1):
            res.append(1)
        else:
            res.append(0)
    return res

def BitDifference (arr1, arr2, univ):
    res = []
    intsec = BitIntersection(arr1, arr2, univ)
    arr1 = BitRepr(arr1, univ)
    for i in range(0, len(univ)):
        if intsec[i] == 0 and arr1[i] == 1 :
            res.append(1)
        else:
            res.append(0)
    return res

def BitToNorm (bitSet,univ):
    res = []
    for i in range(0, len(univ)):
        if bitSet[i] == 1 :
            res.append(univ[i])          
    return res
    
    
def BitSymmetricalDifference(arr1, arr2, univ):
    Union = BitToNorm( BitUnion(arr1, arr2, univ), univ)
    Intersection = BitToNorm( BitIntersection(arr1, arr2, univ), univ)
    Difference = BitDifference(Union, Intersection, univ)
    return Difference
    
    
def Run (arr1, arr2, univ):
    #print(Union(arr1, arr2))
    #print(Intersection(arr1,univ))
    #print(Difference(arr1,univ))
    #print(Complement(univ,arr1))
# =============================================================================
#     print(Difference(arr1,arr2))
#     print(Union(arr1, arr2))
#     print(Intersection(arr1,arr2))    
# =============================================================================
    #print(CartesianProduct(arr1, arr2))
    #print(IsEqual(arr1, arr2))
    #print(IsSubSet(arr2, arr1))
    #print(SymetricalDifference(arr1, arr2))
    #print(BitRepr(arr1, univ))
    #print(BitUnion(arr1,arr2, univ))
    #print(BitIntersection(arr1, arr2, univ))
    #print(BitToNorm( BitDifference(arr1, arr2, univ), univ) )
    print(BitSymmetricalDifference(arr1, arr2, univ))
Run(arr1,arr2, univ)    
