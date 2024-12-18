# Example to find maximum efficiency temp of light bulb
# author: olhartin@asu.edu updated by sdm

import numpy as np                     # for math and arrays
from scipy.integrate import quad       # to integrate
import matplotlib.pyplot as plt        # to plot the curve
from m8_golden import goldsearch       # the golden search function

# Constants used in the calculations
LAMBDA1 = 430e-9                       # lower wavelength
LAMBDA2 = 750e-9                       # upper wavelength
BOLTZ = 1.38064852e-23                 # Boltzmann Constant J/K
C = 2.99792458e8                       # Speed of light in vacuum m/s
PLANCK = 6.626070040e-34               # Planck's Constant J s

# these coefficients are used in the effincandescent_bulb function
COEFF1 = PLANCK*C/(LAMBDA1*BOLTZ)      # so only compute once!
COEFF2 = PLANCK*C/(LAMBDA2*BOLTZ)      # so only compute once!
COEFF3 = 15.0 / ( np.pi**4.0 )         # so only compute once!

################################################################################
# Function to be integrated for lightbulb efficiency                           #
# Input:                                                                       #
#    x - variable inside integrand                                             #
# Output:                                                                      #
#    function evaluated at x                                                   #
################################################################################

def expfun(x):
    return(x**3/(np.exp(x)-1.0))

################################################################################
# Function to perform the lightbulb efficiency integration                     #
# Input:                                                                       #
#    temp - temperature at which to do the calculation                         #
# Output:                                                                      #
#    the efficiency                                                            #
################################################################################

def effincandescent_bulb(temp):
    upperlimit = COEFF1/temp                     # calculate integration limits
    lowerlimit = COEFF2/temp
    res,err = quad(expfun,lowerlimit,upperlimit) # do the integration
    effic = COEFF3 * res                         # mult by constant out front
    return(effic)

# find the temperature of bulb with the peak efficiency
# first look at 300 K, where it is not very efficient
temp = 300
eff = effincandescent_bulb(temp)
print('efficiency {:.3e}'.format(100*eff) + '% at T = ' + str(temp))

# now do the search
T1,T2,T3,T4 = goldsearch(effincandescent_bulb,300,2500,7500,10000,0.001)

T2_eff = effincandescent_bulb(T2)         # efficiency at T2
T3_eff = effincandescent_bulb(T3)         # efficiency at T3
if ( T2_eff > T3_eff ):
    peak_temp = T2                        # this is the peak T and efficiency
    eff_peak  = T2_eff * 100
else:
    peak_temp = T3                        # this is the peak T and efficiency
    eff_peak  = T3_eff * 100

print("max is at : "+ str(round(peak_temp,0)) + " where it is: " +
      str(round(eff_peak,1)) + '%')

print('\nactual filament temperature 2000 to 3300 K')
print('suggesting an efficiency from ' +
        str(round(100*effincandescent_bulb(2000),1)) + '% to '+
        str(round(100*effincandescent_bulb(3300),1)) + '%' )

# plot the efficiency over a range of temperatures from 300 - 10300K
temps = np.linspace(300,10300,50,float) # create a range of interest
Eff = []                                # an empty list to hold efficiencies
for a_temp in temps:                    # for each temperature...
    Eff.append(effincandescent_bulb(a_temp))  # append the efficiency at that T

ax = plt.axes()
ax.set_facecolor('grey')
plt.title(' Efficiency vs Temperature ')  # now create a plot
plt.plot(temps,Eff)
plt.ylabel(' Efficiency ')
plt.xlabel(' Temperature K ')

# place arrow at peak:  plt.arrow(x,y,dx,dy) draws line
plt.arrow(peak_temp,0,0,eff_peak/100,color='blue')

#  place arrow over range of operating temp of 2000 to 3300
eff_op_range = effincandescent_bulb(3300)
plt.arrow(2000,0,1300,0,color='orange')
plt.arrow(3300,0,0,eff_op_range,color='orange')

plt.text(peak_temp+100,.2,"max efficiency",fontsize=24,color="blue")
plt.text(3400,.1,"typical\nefficiency",fontsize=24,color="orange")
plt.show()
