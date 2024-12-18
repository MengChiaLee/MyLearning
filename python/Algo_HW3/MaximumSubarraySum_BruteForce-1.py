#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Meng Chia Lee

from sys import maxsize                        # import max int for initialization

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]        # initialize the input array
ans = -maxsize - 1                             # initialize ans variable to -intmax

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        profit = arr[j] - arr[i]
        if profit > ans: 
            ans = profit

print(ans)                                     # printing the answer