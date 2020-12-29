# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 22:58:34 2020

@author: karup
"""
import pandas as pd
import combinations as cb

df =pd.read_csv("toy_u.csv")

one_activity = []

for case_id in df[df.columns[0]].unique():
    sub = df[df[df.columns[0]]== case_id]
    sub = sub.reset_index(drop=True)
    sub[df.columns[2]] = pd.to_datetime(sub[df.columns[2]] )
    sub = sub.sort_values(by=['time:timestamp'])
    if len(sub)>= 2:
        activity = list(sub['concept:name'])
        if len(sub) >= 2:
            two_comb = cb.two_combination(activity)
        if len(sub) >= 3:
            three_comb = cb.three_combination(activity)
        if len(sub) >= 4:
            four_comb = cb.four_combination(activity)
        if len(sub) >= 5:
            five_comb = cb.five_combination(activity)
        if len(sub) >= 6:
            six_comb = cb.six_combination(activity)
    else:
        one_activity.append(list(sub['concept:name']))

two_combination_unique = cb.ativity_merger(two_comb)
three_combination_unique = cb.ativity_merger(three_comb)
four_combination_unique = cb.ativity_merger(four_comb)
five_combination_unique = cb.ativity_merger(five_comb)

def activity_sequence_comb(df,function_name,combination_unique):
    comb_counts = {}
    for case_id in df[df.columns[0]].unique():
        sub = df[df[df.columns[0]]== case_id]
        sub = sub.reset_index(drop=True)
        #sub[df.columns[2]] = pd.to_datetime(sub[df.columns[2]] )
        #sub = sub.sort_values(by=['time:timestamp'])
        if len(sub)>= 2:
            activity = list(sub['concept:name'])
            if len(sub) >= 2:
                combinations = function_name(activity)
                combinations = cb.ativity_merger(combinations)
                for c in combination_unique:
                    if c in combinations:
                        if c not in comb_counts.keys():
                            comb_counts[c] = 1
                        else:
                            comb_counts[c] += 1
    return comb_counts

result = activity_sequence_comb(df,cb.two_combination,two_combination_unique)