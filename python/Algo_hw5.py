#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: Your Name

w1 = "professor"
w2 = "confession"

# Function to calculate edit distance using Dynamic Programming with memoization
def edit_distance(w1, w2):
    dp = [[0 for _ in range(len(w2) + 1)] for _ in range(len(w1) + 1)]

    # Initialize base cases
    for i in range(len(w1) + 1):
        dp[i][0] = i  # Cost of deleting all characters in w1
    for j in range(len(w2) + 1):
        dp[0][j] = j  # Cost of inserting all characters in w2

    # Fill the memoization table
    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            if w1[i - 1] == w2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(
                    dp[i - 1][j] + 1,    # Delete
                    dp[i][j - 1] + 1,    # Insert
                    dp[i - 1][j - 1] + 1 # Replace
                )
    return dp, dp[len(w1)][len(w2)]

# Backtracking to generate the sequence of operations
def backtrack_operations(w1, w2, dp):
    i, j = len(w1), len(w2)
    operations = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and w1[i - 1] == w2[j - 1]:
            i -= 1
            j -= 1
        elif i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + 1:
            operations.append(f"Replace w1[{i - 1}], '{w1[i - 1]}' with w2[{j - 1}], '{w2[j - 1]}'")
            i -= 1
            j -= 1
        elif j > 0 and dp[i][j] == dp[i][j - 1] + 1:
            operations.append(f"Insert w2[{j - 1}], '{w2[j - 1]}' at {i}")
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            operations.append(f"Delete w1[{i - 1}], '{w1[i - 1]}'")
            i -= 1

    return operations[::-1]

# Calculate the edit distance
dp, min_distance = edit_distance(w1, w2)

# Backtrack to get the operations
operations = backtrack_operations(w1, w2, dp)

# Output results
ans = min_distance  # Store the minimum edit distance in `ans`

print(ans)  # Printing the minimum edit distance
print("Backtrack Operations:")
for op in operations:
    print(op)
