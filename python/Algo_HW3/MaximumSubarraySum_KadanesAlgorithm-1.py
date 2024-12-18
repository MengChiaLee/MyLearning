#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Meng Chia Lee

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array

diff = []                                      #[-2, -5, 6, -2, -3, 1, 5, -6]
for i in range(1, len(arr)):
    diff.append(arr[i] - arr[i-1])

current_max = global_max = diff[0]
start =  end = s = 0

for j in range(1, len(diff)):
    if diff[j] > current_max + diff[j]:
        current_max = diff[j]
        s = j
    else:
        current_max+= diff[j]
    if current_max > global_max:
        global_max = current_max 
        start = s
        end = j 

print(global_max)                         # printing the max possible subarray sum, as ans