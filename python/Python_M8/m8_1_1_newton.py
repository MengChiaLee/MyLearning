# examples of Newton's method for finding zeros
# author: hartin updated by sdm

import numpy as np                       # import math and arrays
import matplotlib.pyplot as plt          # so we can plot
from scipy.optimize import newton        # newton method function

################################################################################
# Function which has a zero when x is an odd multiple of pi                    #
# input: x; returns computed value                                             #
################################################################################
def funcpi(x):
    return(1.0+np.cos(x))

################################################################################
# Function which is the derivative of funcpi                                   #
# input: x; returns the derivative of funcpi at x                              #
################################################################################
def dfuncpi(x):
    return(-np.sin(x))

################################################################################
# A user-defined Newton's Method                                               #
# Inputs:                                                                      #
#   func: the function to use                                                  #
#   dfunc: its derivative                                                      #
#   xstart: starting value, that is, the first guess                           #
#   rconv: convergence rate                                                    #
# Outputs:                                                                     #
#   xn: the root                                                               #
#   num: number of iterations                                                  #
#                                                                              #
# NOTE: There is no safety in this function in case of nonconvergence!         #
################################################################################

def newtmethod(func,dfunc,xstart,rconv,tol):
    xn = xstart                                    # initialize the value
    delta = 1                                      # initialize the difference
    num = 0                                        # initialize the iterations
    while(delta > tol):                            # while too big...
        xnp1 = xn - rconv*func(xn)/dfunc(xn)       # compute next value
        delta = abs(xnp1 - xn)                     # compute the differnce
        xn = xnp1                                  # swap to the next guess
        num += 1                                   # increment the counter
#        print('xn ',xn,' xnp1 ', xnp1, ' delta ', delta)  # debug print

    return(xn,num)                                 # return the results
    
# Find the zero for the function
# sensitive to r! start at 0.1, convergence parameter 1
soln,num = newtmethod(funcpi,dfuncpi,0.1,100,1e-6)
print(' estimate pi ', soln, num)

# this time, start at 0.1, but convergence parameter 0.1
soln,num = newtmethod(funcpi,dfuncpi,0.1,0.1,1e-6)
print(' estimate pi ', soln, num)

# Now use the built in newton's method
soln_ = newton(funcpi,0.1,dfuncpi,tol=1e-6)
print(" built in newton's method ", soln_)

# plot the function
X = np.arange(0,25,0.01)
Y = funcpi(X)
plt.plot(X,Y)
plt.grid()
plt.title("1+cos(x)")
plt.show()
