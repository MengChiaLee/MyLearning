import numpy as np
import matplotlib.pyplot as plt

def integral(a, b, c, r):
    return((a * r**3 / 3) + (b * r**2 / 2) + (c * r)) # after integral

r_step = np.arange(0, 5, 0.01) #because of float so need to use np.arange instead of range
#the first set of parameters
a1, b1, c1 = 2, 3, 4
first_integral = [integral(a1, b1, c1, r)for r in r_step] #r=0.1...5, step=0.01
#the second set of parameters
a2, b2, c2 = 2, 1, 1
second_integral = [integral(a2, b2, c2, r)for r in r_step]

plt.plot(r_step, first_integral, label=f'a={a1}, b={b1}, c={c1}')
plt.plot(r_step, second_integral, label=f'a={a2}, b={b2}, c={c2}')
plt.xlabel('r value')
plt.ylabel('Integral Value')
plt.title('Integral of ax^2 + bx + c from 0 to r')
plt.legend()
plt.show()

