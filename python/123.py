#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Meng Chia Lee

from sys import maxsize  # import max int for initialization

def subarray_maxvalue(diff, low, high):
    if low == high:
        return diff[low]
    mid = (low + high) // 2
    left_sum = subarray_maxvalue(diff, low, mid)
    right_sum = subarray_maxvalue(diff, mid + 1, high)
    cross_sum = cross_maxvalue(diff, low, mid, high)

    return max(left_sum, right_sum, cross_sum)

def cross_maxvalue(diff, low, mid, high):
    left_sum = -maxsize - 1  # initialize ans variable to -intmax
    sum = 0
    for i in range(mid, low - 1, -1):  # Traverse from mid to low
        sum += diff[i]
        if left_sum < sum:
            left_sum = sum

    right_sum = -maxsize - 1  # initialize ans variable to -intmax
    sum = 0
    for i in range(mid + 1, high + 1):  # Traverse from mid+1 to high
        sum += diff[i]
        if right_sum < sum:
            right_sum = sum

    return left_sum + right_sum

arr = [15, 13, 8, 14, 12, 9, 10, 15, 9]  # initialize the input array

diff = []  # [-2, -5, 6, -2, -3, -1, 5, -6]
for i in range(1, len(arr)):
    diff.append(arr[i] - arr[i - 1])

a = len(diff)
ans = subarray_maxvalue(diff, 0, a - 1)
print(ans)  # printing the answer
