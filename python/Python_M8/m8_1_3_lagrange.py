# Example root finder - Langrage point between Earth and Moon
# author: allee updated by sdm

from scipy.optimize import fsolve             # root finder
import matplotlib.pyplot as plt               # plot results
import numpy as np                            # for arrays

G  = 6.674e-11          # gravitational constant
ME = 5.974e24           # mass of earth in kg
MM = 7.348e22           # mass of moon in kg
R  = 3.844e8            # distance to moon in m
OMEGA = 2.662e-6        # rad/s of moon

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
    func = ( ( G * ME ) / ( r**2 ) ) -         \
           ( ( G * MM ) / ( ( R - r )**2 ) ) - \
           ( r * OMEGA**2 )
    return func

# now find the root using an initial guess of 3e8, which is ~78% to the moon
root = fsolve(lagrange_calc,3e8)

# Note that we know that ths problem has exactly one root...
# (fsolve returns an array, but in this case it has only one entry.)

print("distance from earth: {:,}".format(int(root[0])), "meters")
print("distance from moon: {:,}".format(int(R-root[0])), "meters")

# create a plot showing the function across most of the range
x = np.arange(0.5e8, 3.8e8, 0.1e7)
plt.plot(x, lagrange_calc(x)) 
plt.plot([root[0]],[0],marker='x',markersize=20,c='red')
plt.plot([R],[0],marker='o',markersize=5,c='black',label='distance to moon')
plt.xlabel('distance from sun')
plt.ylabel('residual')
plt.xlabel('distance from earth')
plt.ylabel('residual')
plt.title('Earth-Moon Lagrange Point')
plt.show()

