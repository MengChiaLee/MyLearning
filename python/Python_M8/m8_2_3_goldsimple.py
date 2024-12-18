# Example to find maximum efficiency temp of light bulb
# author: olhartin@asu.edu updated by sdm

import numpy as np                     # for math and arrays
from m8_2_2_golden import goldsearch       # the golden search function

################################################################################
# A test function to find a max for... Clearly, the max is at x = 2.           #
# Input:                                                                       #
#    x - value at which to evaluate the function                               #
# Output:                                                                      #
#    the value of the function evaluated at x                                  #
################################################################################

def func(x):
    return(float(10.0-(x-2.0)**2))
    
x1,x2,x3,x4 = goldsearch(func,0,1,2,2.5,0.001)     # now find the max
print("max is at : ",max(x2,x3), "where it is f(x): ", func(max(x2,x3)))
