import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize
import pandas as pd

# Constants
KB = 1.380648e-23    # Boltzmann constant (J/K)
Q = 1.6021766208e-19 # Electron charge (C)

# Problem 1 Parameters
P1_IS = 1e-9         # Reverse bias saturation current (A)
P1_N = 1.7          # Ideality factor (unitless), indicates how closely the diode follows the ideal diode equation
P1_R = 11000        # Resistance in ohms (Ω)
P1_T = 350          # Temperature in Kelvin (K)
P1_V_START = 0.1    # Starting voltage (V)
P1_V_END = 2.5      # Ending voltage (V)
P1_V_STEP = 0.1     # Voltage step (V)

# Problem 2 Parameters
P2_AREA = 1e-8      # Diode area (m^2)
P2_T = 375          # Temperature (K)
P2_PHI_INIT = 0.8   # Initial barrier height (phi) guess (V)
P2_N_INIT = 1.5     # Initial ideality factor guess (unitless)
P2_R_INIT = 10000   # Initial resistance guess (Ω)

def diode_current(v_d, n, t, i_s):
    """Calculate diode current using the diode equation. """
    v_t = n * KB * t / Q  # Thermal voltage (V)
    return i_s * (np.exp(v_d / v_t) - 1)  # Diode current equation

def solve_diode_v(v_d, v_s, r, n, t, i_s):
    """Function to solve for diode voltage using nodal analysis."""
    i_d = diode_current(v_d, n, t, i_s)  # Calculate diode current
    return i_d - (v_s - v_d) / r  # Current balance equation using Ohm's law

def problem1():
    """Solve Problem 1: Calculate and plot the diode current vs. source voltage and diode voltage."""
    # Create an array of source voltages
    v_source = np.arange(P1_V_START, P1_V_END + P1_V_STEP, P1_V_STEP)
    v_diode = np.zeros_like(v_source)  # Array to store diode voltages
    i_diode = np.zeros_like(v_source)  # Array to store diode currents
    
    # Initial guess for diode voltage
    prev_v = P1_V_STEP  # Start with a small voltage as an initial guess
    
    # Solve for each voltage point
    for i, v_s in enumerate(v_source):
        # Use fsolve to find the diode voltage that satisfies the circuit equation
        prev_v = optimize.fsolve(solve_diode_v, prev_v, 
                               args=(v_s, P1_R, P1_N, P1_T, P1_IS),
                               xtol=1e-12)[0]
        v_diode[i] = prev_v  # Store the calculated diode voltage
        i_diode[i] = diode_current(v_diode[i], P1_N, P1_T, P1_IS)  # Calculate and store the diode current
    
    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.semilogy(v_source, i_diode, 'b-', label='log(Diode Current) vs Source Voltage')
    plt.semilogy(v_diode, i_diode, 'r--', label='log(Diode Current) vs Diode Voltage')
    plt.grid(True)
    plt.xlabel('Voltage (V)')
    plt.ylabel('Diode Current')
    plt.legend()
    plt.title('Problem 1')
    plt.show()
    
    return v_source, v_diode, i_diode

def DiodeI(Vd, A, phi, n, T):
    """Calculate the diode current for given parameters."""
    Vt = n * KB * T / Q  # Thermal voltage (V)
    Is = A * T * T * np.exp(-phi * Q / (KB * T))  # Saturation current (A)
    return Is * (np.exp(Vd / Vt) - 1)  # Diode current equation

def compute_current_for_params(v_source, A, phi, n, R, T):
    """Compute diode current for given parameters over a range of source voltages."""
    v_diode = np.zeros_like(v_source)  # Array to store diode voltages
    prev_v = P1_V_STEP  # Initial guess for diode voltage
    
    for i, v_s in enumerate(v_source):
        # Define a function to solve for diode voltage
        def solve_v(v_d):
            i_d = DiodeI(v_d, A, phi, n, T)  # Calculate diode current
            return i_d - (v_s - v_d) / R  # Balance equation for current through resistor and diode
        
        prev_v = optimize.fsolve(solve_v, prev_v, xtol=1e-12)[0]  # Find diode voltage
        v_diode[i] = prev_v  # Store diode voltage
    
    return DiodeI(v_diode, A, phi, n, T)  # Return computed diode currents

def residual_phi(phi_val, n_val, r_val, area, temp, source_v, meas_i):
    """Residual function for optimizing the barrier height (phi)."""
    calc_i = compute_current_for_params(source_v, area, phi_val, n_val, r_val, temp)  # Calculate diode currents
    return (calc_i - meas_i) / (calc_i + meas_i + 1e-15)  # Normalized residuals to account for small values

def residual_n(n_val, phi_val, r_val, area, temp, source_v, meas_i):
    """Residual function for optimizing the ideality factor (n). """
    calc_i = compute_current_for_params(source_v, area, phi_val, n_val, r_val, temp)  # Calculate diode currents
    return (calc_i - meas_i) / (calc_i + meas_i + 1e-15)  # Normalized residuals

def residual_r(r_val, n_val, phi_val, area, temp, source_v, meas_i):
    """Residual function for optimizing the resistance (R)."""
    
    calc_i = compute_current_for_params(source_v, area, phi_val, n_val, r_val, temp)  # Calculate diode currents
    return (calc_i - meas_i) / (calc_i + meas_i + 1e-15)  # Normalized residuals

def problem2():
    """Solve Problem 2: Optimize the parameters of the diode and plot the results."""
    # Load measured data from file
    data = pd.read_csv('DiodeIV.txt', sep='\s+', header=None, dtype=np.float64)
    source_v = data[0].values  # Source voltages (V)
    meas_i = data[1].values  # Measured currents (A)
    
    # Initial parameter guesses
    phi_val = P2_PHI_INIT  # Initial guess for barrier height
    n_val = P2_N_INIT  # Initial guess for ideality factor
    r_val = P2_R_INIT  # Initial guess for resistance
    
    # Optimization loop
    max_iter = 100  # Maximum number of iterations
    tolerance = 1e-6  # Tolerance for parameter changes
    iteration = 0  # Iteration counter
    err = float('inf')  # Initial error value
    
    while err > tolerance and iteration < max_iter:
        old_params = np.array([phi_val, n_val, r_val])  # Store old parameter values
        
        # Optimize barrier height (phi)
        phi_opt = optimize.leastsq(residual_phi, phi_val,
                                 args=(n_val, r_val, P2_AREA, P2_T, source_v, meas_i))
        phi_val = phi_opt[0][0]  # Update phi value
        
        # Optimize ideality factor (n)
        n_opt = optimize.leastsq(residual_n, n_val,
                               args=(phi_val, r_val, P2_AREA, P2_T, source_v, meas_i))
        n_val = n_opt[0][0]  # Update n value
        
        # Optimize resistance (R)
        r_opt = optimize.leastsq(residual_r, r_val,
                               args=(n_val, phi_val, P2_AREA, P2_T, source_v, meas_i))
        r_val = r_opt[0][0]  # Update R value
        
        # Calculate error as the mean absolute difference between new and old parameters
        new_params = np.array([phi_val, n_val, r_val])  # New parameter values
        err = np.mean(np.abs(new_params - old_params))  # Calculate error
        print(f"Iteration {iteration}: phi={phi_val:.6f}, n={n_val:.6f}, R={r_val:.2f}")  # Print progress
        
        iteration += 1  # Increment iteration counter
    
    # Plot final results
    calc_i = compute_current_for_params(source_v, P2_AREA, phi_val, n_val, r_val, P2_T)  # Calculate predicted currents
    
    fig, ax1 = plt.subplots(figsize=(10, 6))
    
    # Plot measured data on left y-axis
    ax1.semilogy(source_v, meas_i, 'bo', label='Measured Current')
    ax1.set_xlabel('Voltage (volts)')
    ax1.set_ylabel('Measure Current ', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    
    # Create right y-axis and plot predicted data
    ax2 = ax1.twinx()
    ax2.semilogy(source_v, calc_i, 'r-', label='Predicted Current')
    ax2.set_ylabel('Predicted Current ', color='orange')
    ax2.tick_params(axis='y', labelcolor='orange')
    plt.title('Problem 2')
    plt.show()
    
    return phi_val, n_val, r_val

if __name__ == "__main__":
    # Solve Problem 1
    print("Solving Problem 1...")
    v_source, v_diode, i_diode = problem1()
    
    # Solve Problem 2
    print("\nSolving Problem 2...")
    phi, n, r = problem2()
    print(f"\nFinal Parameters:")
    print(f"Phi = {phi:.6f}")
    print(f"n = {n:.6f}")
    print(f"R = {r:.2f} ohms")