################################################################################
# Created on Fri Aug 24 13:36:53 2018                                          #
#                                                                              #
# @author: olhartin@asu.edu; updates by sdm                                    #
#                                                                              #
# Program to solve resister network with voltage and/or current sources        #
################################################################################

import numpy as np                     
from numpy.linalg import solve         # solve is used for solve linear algebra problem
from read_netlist import read_netlist  
import comp_constants as COMP          

# this is the list structure that we'll use to hold components:
# [ Type, Name, i, j, Value ]

################################################################################
# How large a matrix is needed for netlist? This could have been calculated    #
# at the same time as the netlist was read in but we'll do it here             #
# Input:                                                                       #
#   netlist: list of component lists                                           #
# Outputs:                                                                     #
#   node_cnt: number of nodes in the netlist                                   #
#   volt_cnt: number of voltage sources in the netlist                         #
################################################################################

def get_dimensions(netlist):           #to know how N*N is
    node_cnt = 0    
    volt_cnt = 0

    for comp in netlist:
        # finding the maximun [i][j] = node_cnt
        node_cnt = max(node_cnt, comp[COMP.I], comp[COMP.J])

        # finding how many voltage source
        if comp[COMP.TYPE] == COMP.VS:
            volt_cnt += 1

    return node_cnt, volt_cnt


################################################################################
# Function to stamp the components into the netlist                            #
# Input:                                                                       #
#   y_add:    the admittance matrix                                            #
#   netlist:  list of component lists                                          #
#   currents: the matrix of currents                                           #
#   node_cnt: the number of nodes in the netlist                               #
# Outputs:                                                                     #
#   node_cnt: the number of rows in the admittance matrix                      #
################################################################################

def stamper(y_add,netlist,currents,node_cnt):
    # return the total number of rows in the matrix for
    # error checking purposes
    # add 1 for each voltage source...

    for comp in netlist:                  # for each component...
        #print(' comp ', comp)            # which one are we handling...

        # extract the i,j and fill in the matrix...
        # subtract 1 since node 0 is GND and it isn't included in the matrix
        i = comp[COMP.I] - 1
        j = comp[COMP.J] - 1

        if ( comp[COMP.TYPE] == COMP.R ):           # a resistor
            if (i >= 0):                            # add on the diagonal
                y_add[i,i] += 1.0 / comp[COMP.VAL]
            if (j >= 0):                            # add on the diagonal
                y_add[j,j] += 1.0 / comp[COMP.VAL]
            if (i >= 0 and j >= 0):                 # add off-diagonal
                y_add[i,j] -= 1.0 / comp[COMP.VAL]
                y_add[j,i] -= 1.0 / comp[COMP.VAL]
        
        elif (comp[COMP.TYPE] == COMP.VS):          # a voltage source
            vs_index = node_cnt                     # index for voltage sources in the matrix
            if i >= 0:
                y_add[i, vs_index] = 1.0            # mark in the matrix
                y_add[vs_index, i] = 1.0
            if j >= 0:
                y_add[j, vs_index] = -1.0           # mark in the matrix
                y_add[vs_index, j] = -1.0

            # The current value of the voltage source should be recorded in the current vector.
            currents[vs_index] = comp[COMP.VAL]
            node_cnt += 1                           # increase array to statified voltage sources

        elif (comp[COMP.TYPE] == COMP.IS):          # a current source
            if i >= 0:
                currents[i] -= comp[COMP.VAL]       # The current flows out from i.
            if j >= 0:
                currents[j] += comp[COMP.VAL]       # The current flows out from j.

    return node_cnt  # should be same as number of rows!

################################################################################
# Start the main program now...                                                #
################################################################################

# Read the netlist!
netlist = read_netlist()

# Print the netlist so we can verify we've read it correctly
for index in range(len(netlist)):
    print(netlist[index])
print("\n")
# Get the dimensions (number of nodes and voltage sources)
node_cnt, volt_cnt = get_dimensions(netlist)

# Initialize the admittance matrix (y_add) and the currents vector
# y_add size is node_cnt + volt_cnt to account for extra rows for voltage sources
y_add = np.zeros((node_cnt + volt_cnt, node_cnt + volt_cnt))
currents = np.zeros(node_cnt + volt_cnt)

# Stamp the components into the admittance matrix and currents vector
total_rows = stamper(y_add, netlist, currents, node_cnt)

# Solve the system of linear equations to get the voltage vector
voltage_vector = solve(y_add, currents)

# Print the voltage vector as the output
print(voltage_vector[:node_cnt])

