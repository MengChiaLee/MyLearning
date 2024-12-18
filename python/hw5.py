import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Problem 1: y' = cos(t), y(0) = 1
def deriv1(y, t):
    return np.cos(t)

# Problem 2: y' = -y + t²e^(-2t) + 10, y(0) = 0
def deriv2(y, t):
    return -y + (t**2) * np.exp(-2*t) + 10

# Problem 3: y'' + 4y' + 4y = 25cos(t) + 25sin(t), y(0) = 1, y'(0) = 1
def deriv3(state, t):
    y, dy = state  # unpack state vector
    # Calculate second derivative from the ODE
    d2y = 25*np.cos(t) + 25*np.sin(t) - 4*dy - 4*y
    return [dy, d2y]

# Create time vector (0 to 7 with 700 points)
t = np.linspace(0, 7, 700)

# Solve Problem 1
y1 = odeint(deriv1, 1, t)

# Solve Problem 2
y2 = odeint(deriv2, 0, t)

# Solve Problem 3 (need to solve as system of first-order ODEs)
y3 = odeint(deriv3, [1, 1], t)  # Initial conditions: y(0)=1, y'(0)=1

# Create plots
plt.figure(figsize=(15, 5))

# Problem 1
plt.subplot(131)
plt.plot(t, y1, 'b-', label='y(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Problem 1: y\' = cos(t)')
plt.grid(True)
plt.legend()

# Problem 2
plt.subplot(132)
plt.plot(t, y2, 'r-', label='y(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Problem 2: y\' = -y + t²e^(-2t) + 10')
plt.grid(True)
plt.legend()

# Problem 3
plt.subplot(133)
plt.plot(t, y3[:, 0], 'g-', label='y(t)')
plt.plot(t, y3[:, 1], 'b--', label='y\'(t)')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Problem 3: y\'\' + 4y\' + 4y = 25cos(t) + 25sin(t)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()