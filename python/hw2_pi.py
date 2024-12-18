import numpy as np
from scipy.integrate import quad


def integrand(z):   #the integral function after substitution
    return np.sqrt(z) / (z*(np.sqrt(1-z)))

result,_= quad(integrand, 0, 1) #integral

print(f"pi is: {np.pi:.8f}") #the question ask the pi have to print 8 deicmal places

difference = np.abs(result - np.pi) #result-pi
print(f"Difference from numpy.pi is: {difference:.15f}")    #the question ask the difference of result have to print 15 decimal places
