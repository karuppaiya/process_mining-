# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:49:11 2020

@author: karup
"""

def two_combination(activity):
    two_comb = []
    for i in range(len(activity)-1):
        if i == 0:
            two_comb.append([activity[i],activity[i+1]])
        else:
            two_comb.append([activity[i],activity[i+1]])
    return two_comb

def three_combination(activity):
    three_comb = []
    for i in range(len(activity)-2):
        if i == 0:
            three_comb.append([activity[i],activity[i+1],activity[i+2]])
        else:
            three_comb.append([activity[i],activity[i+1],activity[i+2]])
    return three_comb

def four_combination(activity):
    four_comb = []
    for i in range(len(activity)-3):
        if i == 0:
            four_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3]])
        else:
            four_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3]])
    return four_comb

def five_combination(activity):
    five_comb = []
    for i in range(len(activity)-4):
        if i == 0:
            five_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4]])
        else:
            five_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4]])
    return five_comb

def six_combination(activity):
    six_comb = []
    for i in range(len(activity)-5):
        if i == 0:
            six_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4],activity[i+5]])
        else:
            six_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4],activity[i+5]])
    return six_comb

def seventh_combination(activity):
    seven_comb = []
    for i in range(len(activity)-5):
        if i == 0:
            seven_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4],activity[i+5],activity[i+6]])
        else:
            seven_comb.append([activity[i],activity[i+1],activity[i+2],activity[i+3],activity[i+4],activity[i+5],activity[i+6]])
    return seven_comb

def ativity_merger(combinations_list):
    
    # Merging activities
    after_merge = []
    for i in combinations_list:
        after_merge.append(''.join(i))
    
    # Removing duplicates
    final = [] 
    for i in after_merge: 
        if i not in final: 
            final.append(i) 
        
    return final