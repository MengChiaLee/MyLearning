import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt

# 70 years retirememt
MAX_YEARS = 70

# Function to simulate wealth growth
def calculate_wealth(mean_return, Std_dev, yearly_contribution, contribution_years, retirement_years, annual_spend):
    all_wealths = []
    
    # 10 analyses
    for _ in range(10):
        wealth = np.zeros(MAX_YEARS)
        noise = (Std_dev / 100) * np.random.randn(MAX_YEARS)
        
        # Contributions phase
        for i in range(contribution_years):
            wealth[i+1] = wealth[i] * (1 + mean_return / 100 + noise[i]) + yearly_contribution
        
        # Post-contribution, pre-retirement phase
        for i in range(contribution_years, retirement_years):
            wealth[i+1] = wealth[i] * (1 + mean_return / 100 + noise[i])
        
        # Retirement phase (spending)
        for i in range(retirement_years, MAX_YEARS - 1):
            wealth[i+1] = wealth[i] * (1 + mean_return / 100 + noise[i]) - annual_spend
            if wealth[i+1] < 0:
                wealth[i+1] = 0
                break
        
        all_wealths.append(wealth)
    
    avg_wealth = np.mean([w[retirement_years-1] for w in all_wealths])
    
    # Plot the wealth over time for each simulation
    plt.figure(figsize=(10,6))
    for w in all_wealths:
        plt.plot(range(MAX_YEARS), w)
    
    plt.xlabel('Year')
    plt.ylabel('Wealth ($)')
    plt.title('Wealth over Time (10 Simulations)')
    plt.axhline(0, color='black', lw=0.5)
    plt.show()
    
    return avg_wealth

# GUI Layout and Functions
def calculate_and_display():
    try:
        # Get input values
        mean_return = float(entry_mean_return.get())
        Std_dev = float(entry_Std_dev.get())
        yearly_contribution = float(entry_yearly_contribution.get())
        contribution_years = int(entry_contribution_years.get())
        retirement_years = int(entry_retirement_years.get())
        annual_spend = float(entry_annual_spend.get())
        
        # Run the calculation
        avg_wealth = calculate_wealth(mean_return, Std_dev, yearly_contribution, contribution_years, retirement_years, annual_spend)
        
        # Display the result immediately after calculation
        label_avg_wealth.config(text=f'Wealth at retirement: ${avg_wealth:,.2f}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# main window
root = tk.Tk()
root.title("Wealth Calculator")

# Create and place widgets
tk.Label(root, text="Mean Return (%)").grid(row=0, column=0, padx=10, pady=5, sticky='e')
entry_mean_return = tk.Entry(root)
entry_mean_return.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Std Dev Return (%)").grid(row=1, column=0, padx=10, pady=5, sticky='e')
entry_Std_dev = tk.Entry(root)
entry_Std_dev.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Yearly Contribution ($)").grid(row=2, column=0, padx=10, pady=5, sticky='e')
entry_yearly_contribution = tk.Entry(root)
entry_yearly_contribution.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="No. of Years of Contribution").grid(row=3, column=0, padx=10, pady=5, sticky='e')
entry_contribution_years = tk.Entry(root)
entry_contribution_years.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="No. of Years to Retirement").grid(row=4, column=0, padx=10, pady=5, sticky='e')
entry_retirement_years = tk.Entry(root)
entry_retirement_years.grid(row=4, column=1, padx=10, pady=5)

tk.Label(root, text="Annual Retirement Spend ($)").grid(row=5, column=0, padx=10, pady=5, sticky='e')
entry_annual_spend = tk.Entry(root)
entry_annual_spend.grid(row=5, column=1, padx=10, pady=5)

# Result label
label_avg_wealth = tk.Label(root, text="Wealth at retirement: ")
label_avg_wealth.grid(row=6, column=0, columnspan=2, pady=10)  # Adjust columnspan to 2

# Buttons
frame_buttons = tk.Frame(root)
frame_buttons.grid(row=7, column=0, columnspan=2, pady=10)

tk.Button(frame_buttons, text="Quit", command=root.quit).grid(row=0, column=0, padx=10)
tk.Button(frame_buttons, text="Calculate", command=calculate_and_display).grid(row=0, column=1, padx=10)  # Adjust padding

# Start the GUI event loop
root.mainloop()
