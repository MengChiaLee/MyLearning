import numpy as np #import numpy for np.abs(absolute value)

N = int(input("Enter a number whose square root is desired: "))#input N
guess = int(input("Enter an initial guess: "))# input ni
tolerance = 0.01 #input ε

def my_sqrt(N, guess, tolerance):
    #to check whether if in the tolerance
    next_guess = (guess + N / guess) / 2 #next guess is ni+1
    if np.abs(next_guess - guess) < tolerance:
        return next_guess
    else:   #if not in the tolerance then return back and use new value to do again
        return my_sqrt(N, next_guess, tolerance)

result = my_sqrt(N, guess, tolerance)

print(f"The square root of{N}is {result:.2f}")  #{result:.2f}is to make the result can have 2 decimal just like example
