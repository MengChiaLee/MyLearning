# Example root finder - Langrage point between Earth and Moon
# author: allee updated by sdm

from scipy.optimize import fsolve             # root finder
import numpy as np                            # for arrays
import matplotlib.pyplot as plt               # plot results

G  = 6.674e-11          # gravitational constant
ME = 5.974e24           # mass of earth in kg
MS = 1.981e30           # mass of sun in kg
R  = 1.495e11           # distance to sun in m
OMEGA = 1.99e-7         # rad/s of earth

################################################################################
# Function which is force between earth and moon to find the zero              #
# Input:                                                                       #
#    r - the radius to try, that is, distance from earth                       #
# Output:                                                                      #
#    func - the result of the function - trying to make it 0                   #
#                                                                              #
# Note that the equation used was derived in class...                          #
################################################################################

def lagrange_calc(r):
    func = ( ( G * MS ) / ( r**2 ) ) -         \
           ( ( G * ME ) / ( ( R - r )**2 ) ) - \
           ( r * OMEGA**2 )
    return func

# now find the root using an initial guess of 3e10, which is ~20% to the sun
root = fsolve(lagrange_calc,3e10)

# Note that we know that ths problem has exactly one root...
# (fsolve returns an array, but in this case it has only one entry.)

print("distance from sun: {:,}".format(int(root[0])), "meters")
print("distance from earth: {:,}".format(int(R-root[0])), "meters")

# create a plot showing the function across most of the range
x = np.arange(0.5e10, 2.0e11, 0.1e10)
plt.plot(x, lagrange_calc(x)) 
plt.plot([root[0]],[0],marker='x',markersize=20,c='red',label='lagrange point')
plt.plot([R],[0],marker='o',markersize=5,c='black',label='distance to sun')
plt.xlabel('distance from sun')
plt.ylabel('residual')
plt.legend()
plt.title('Sun-Earth Lagrange Point')
plt.show()

