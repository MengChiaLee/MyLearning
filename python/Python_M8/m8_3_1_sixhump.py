# Example from scipy.org for nonlinear optimization - find the minimum
# from Allee, updated by sdm

import numpy as np                       # for arrays
from scipy import optimize               # access to optimization functions
import matplotlib.pyplot as plt          # to create the plot
from mpl_toolkits.mplot3d import Axes3D  # to allow 3D!

################################################################################
# Function to implement the 6-hump shape from which to find the minimum        #
# Input:                                                                       #
#    coords - x and y value at which to evaluate the function                  #
# Output:                                                                      #
#    the value of the function                                                 #
################################################################################

def sixhump(coords):
    x = coords[0]             # extract the x and y for clarity
    y = coords[1]
    return ( 4 - ( 2.1 * x**2 ) + ( x**4 / 3. ) ) * x**2 +  \
           x * y +                                          \
           (-4 + ( 4 * y**2 ) ) * y**2

# create a meshgrid so we have two arrays from which we can project the surface
x = np.linspace(-2, 2)      # allow x to vary from -2 to 2
y = np.linspace(-1, 1)      # allow y to vary from -1 to 1
xg, yg = np.meshgrid(x, y)  # create the meshgrid

plt.figure()                   # simple visualization in 2D
plt.imshow(sixhump([xg, yg]))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y',rotation=0)
plt.title('six hump in 2D')
plt.show()

# First optimization using bfgs with initial guess 2,-1, disp=0 for quiet
result = optimize.fmin_bfgs(sixhump, [2,-1], disp=0)
print('bfgs result:',result)

# Second optimization using basin hopping with initial guess 2,-1
result = optimize.basinhopping(sixhump, [2,-1])
print(type(result))                        # this is a significant structure
print('basin hopping result:',result.x)    # many other attributes generated

fig = plt.figure()                         # awesome visulization in 3D
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(xg, yg, sixhump([xg, yg]), rstride=1, cstride=1,
                       cmap=plt.cm.jet, linewidth=0, antialiased=False)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.zaxis.set_rotate_label(False)
ax.set_zlabel('f(x, y)')
ax.set_title('Six-hump Camelback function')
plt.show()
