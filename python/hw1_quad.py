from math import sqrt   #import math because I want use √
import cmath            #import cmath for √(-1) = i in python is j

a = int(input("input coefficient a: "))
b = int(input("input coefficient b: "))
c = int(input("input coefficient c: "))

b_square = b**2
discriminan = b_square - 4*a*c #The case where there are two roots
if discriminan > 0:
    x1 = (-b + sqrt(discriminan)) / (2*a) #quadratic formula
    x2 = (-b - sqrt(discriminan)) / (2*a)
    print("Root 1: ", float(x1)) 
    print("Root 1: ", float(x2))

elif discriminan == 0:  #The case where there only one root 
    x = (-b / (2*a))    # because b_square - 4*a*c = 0 so I just ignore
    print("Double root: ", float(x))

else:   #The case where there are complex roots
    real_num = (-b) / (2*a) #complex roots which is made by real number plus imaginary number
    imaginary_num = cmath.sqrt(discriminan) / (2*a) # cmath.sqrt(-1) = 1i = √(-1)
    x1 = real_num + imaginary_num
    x2 = real_num - imaginary_num
    print("Root 1: ", x1) 
    print("Root 1: ", x2)
    

