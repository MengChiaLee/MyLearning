#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#author: Meng Chia Lee

''' --- Input values --- '''
M = [ [2, 1, 4, 5, 3],  # Department preference list
      [4, 2, 1, 3, 5],
      [2, 5, 3, 4, 1],
      [1, 4, 3, 2, 5],
      [2, 4, 1, 5, 3] ]

W = [ [5, 1, 2, 4, 3],  # Employee preference list
      [3, 2, 4, 1, 5],
      [2, 3, 4, 5, 1],
      [1, 5, 4, 3, 2],
      [4, 2, 5, 3, 1] ]

N = 5  # Number of departments & employees

free_dept = list(range(N))          #列出友還尚未招募到員工的department
current_emp_array = [-1] * N     #記錄目前員工跟哪個department配對
current_dept_array = [-1] * N    #紀錄目前dpartment跟哪個員工配對
dept_recruit = [0] * N              #紀錄department招募第幾個員工

employ_rank = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        employ_rank[i][(W[i][j]-1)] = j  #我要幫員工的preference list弄成一個index

#Gale-Shapley部門優先演匴法
while free_dept:
    dept = free_dept.pop(0) #dept就是目前正要配對的公司/ current_dept目前正在配對再一起的
    dept_choice = M[dept][dept_recruit[dept]] - 1
    dept_recruit[dept] += 1

    if current_emp_array[dept_choice] == -1:
        current_emp_array[dept_choice] = dept
        current_dept_array[dept] =  dept_choice

    else:
        current_dept = current_emp_array[dept_choice] 
        if  employ_rank[dept_choice][current_dept] > employ_rank[dept_choice][dept] : #正要配對vs已配對   
            current_emp_array[dept_choice] = dept
            current_dept_array[dept] =  dept_choice
            free_dept.append(current_dept)
        else:  
            free_dept.append(dept)

Names = [['HR', 'CRM', 'Admin', 'Research', 'Development'],  
         ['Adam', 'Bob', 'Clare', 'Diane', 'Emily']]

print('Result is:-')
for i in range(N):
    print(Names[0][i], ":", Names[1][current_dept_array[i]])