# nonlinear least squares example
# perhaps similar to david gay dn2fb
# author: allee@asu.edu updated by sdm

import numpy as np                    # math and arrays
from scipy.optimize import leastsq    # optimization function
import matplotlib.pyplot as plt       # so we can plot

N=1000                                # number of samples to generate

################################################################################
# Function to fit                                                              #
# Inputs:                                                                      #
#    kd - first value, which we are trying to determine                        #
#    p0 - second value, which is the known domain                              #
# Output:                                                                      #
#    value of the function                                                     #
################################################################################

def func(kd,p0):
    return 0.5*(-1-((2*p0)/kd) + np.sqrt(4*(p0/kd)+(((2*p0)/kd)-1)**2))

################################################################################
# Function to compute the difference between the actual and predicted values   #
# Inputs:                                                                      #
#    kd_guess - the guess for the value of the first parameter                 #
#    p0 - the second parameter, which is known                                 #
#    actual - the sampled value                                                #
# Output:                                                                      #
#    difference between the actual value and the value calculated with guess   #
################################################################################

def residuals(kd_guess,p0,actual):
    return actual - func(kd_guess,p0)

# Create a noisy signal based on a known value of kd of 3
# since random returns uniformly distributed [0,1), subtract .5 gives
# [-.5,.5) so we get +/- noise
kd=3.0                                                # the "known" value
p0 = np.linspace(0,10,N)                              # an array for p0
clean = func(kd,p0)                                   # the clean signal
actual = clean+(np.random.random(N)-0.5)*1.0          # the noisy signal

# now try to extract the the known value of kd by minimizing the residuals
# residuals - the function we are optimizing
# 5 - the initial guess for the value to find, in this case, kd
# args - the additional arguments needed, in this case the x and y values
# full_output - return all the outputs
kd_match,cov,infodict,mesg,ier = leastsq(residuals,5,args=(p0,actual),
                                         full_output=True)

print("actual kd was",kd)                      # original value
print('kd guess', kd_match)                    # this is the guess for kd
# print('cov\n',cov)                           # inversion of the Hession
# print('infodict\n',infodict)                 # various other outputs
print('mesg\n',mesg)                           # a string with status
print('ier\n',ier)                             # status flag

plt.plot(p0,actual)                            # plot the noisy signal
plt.plot(p0,func(kd_match,p0))                 # along with the estimate
plt.xlabel('p0')
plt.ylabel('func(p0)')
plt.title('noisy signal and estimate')
plt.show()

plt.plot(p0,func(kd_match,p0),label='estimate')  # plot the estimate
plt.plot(p0,clean,label='original')              # with clean signal
plt.xlabel('p0')
plt.ylabel('func(p0)')
plt.legend()
plt.title('clean original and estimate')
plt.show()

# difference between predicted value and received value
resid = residuals(kd_match,p0,actual)          # calculate the residuals
plt.plot(p0,resid)                             # and plot them
plt.xlabel('p0')
plt.ylabel('residual')
plt.title('predicted vs received residuals')
plt.show()

# difference between the predicted value adn the clean value
resid = residuals(kd_match,p0,clean)           # calculate the residuals
plt.plot(p0,resid)                             # and plot them
plt.xlabel('p0')
plt.ylabel('residual')
plt.title('predicted vs clean residuals')
plt.show()
