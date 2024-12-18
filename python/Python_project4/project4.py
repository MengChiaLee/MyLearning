import numpy as np
import subprocess
import os

# global constants
MAX_FAN = 8     # max value for fan 
MAX_INV = 12    # max value for number of inverters
INPUT_FILE_NAME = 'header.sp'           # initial input filename
OUTPUT_FILE_NAME = 'InvChain.mt0.csv'   # output filename
HSPICE_INPUT_FILE_NAME = 'InvChain.sp'  # file to use in hspice simulation

def extract_tphl():
    """Return tphl value from hspice output file"""
    data = np.recfromcsv(OUTPUT_FILE_NAME, comments="$", skip_header=3)
    tphl = data["tphl_inv"]
    return tphl

def run_hspice():
    """Run hspice simulation for current fan & no of inverters"""
    proc = subprocess.Popen(["hspice", HSPICE_INPUT_FILE_NAME],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = proc.communicate()

def prepare_simulation_input(netlist, fan, N):
    """Generate netlist for fan & inverters combination"""
    # add .param line to hspice file
    netlist += f'\n\n.param fan = {fan}\n'

    # add inverters based on N value
    if (N == 1):
        netlist += 'Xinv1 a z inv M=1\n'
    else:
        # start ascii number for node a
        start = ord('a')
        # add first inverter a -> b
        netlist += 'Xinv1 a b inv M=1\n'
        for inv in range(2, N):
            # add next inverter
            netlist += f'Xinv{inv} {chr(start+1)} {chr(start+2)} inv M=fan**{inv-1}\n'
            # increase current node char ASCII code
            start += 1
        # add last inverter
        netlist += f'Xinv{N} {chr(start+1)} z inv M=fan**{N-1}\n'
    
    # end netlist
    netlist += '.end\n'

    # write netlist to file
    with open(HSPICE_INPUT_FILE_NAME, 'w') as file:
        file.write(netlist)

def read_netlist():
    """Read hspice initial file"""
    with open(INPUT_FILE_NAME, 'r') as file:
        return file.read()

def optimize_chain():
    """Find optimal N and fan values"""
    # create fan list & num of inverters list
    fan_list = [fan for fan in range(2, MAX_FAN)]                    # fan list
    inv_list = [inv for inv in range(0, MAX_INV) if inv % 2 != 0]   # inv list

    # prepare minimum delay & optimal parameters
    min_delay = float('inf')
    optimal_fan = 0
    optimal_N = 0
    results = []

    # read netlist
    netlist = read_netlist()

    # loop over fan & inverters combinations
    for inv in inv_list:
        for fan in fan_list:
            # prepare netlist hspice file
            prepare_simulation_input(netlist, fan, inv)

            # run hspice simulation
            run_hspice()

            # wait for output file
            while not os.path.isfile(OUTPUT_FILE_NAME):
                pass

            # extract tphl
            tphl = extract_tphl()
            results.append((inv, fan, tphl))

            print(f'N {inv: <{2}} fan {fan: <{1}} tphl {tphl: <{10}}')

            # update optimal values if better delay found
            if tphl < min_delay:
                min_delay = tphl
                optimal_fan = fan
                optimal_N = inv

    return (optimal_N, optimal_fan), min_delay, results

def write_results_to_file(best_config, best_delay, results):
    """Write simulation results and best configuration to output.txt"""
    with open("output.txt", "w") as file:
        for N, fan, delay in results:
            file.write(f'N {N}  fan {fan} tphl {delay:.3e}\n')
        
        file.write("\nBest values were:\n")
        file.write(f'\tfan = {best_config[1]}\n')
        file.write(f'\tnum_inverters = {best_config[0]}\n')
        file.write(f'\ttphl = {best_delay:.3e}\n')

def main():
    print("Starting inverter chain optimization...")
    
    best_config, best_delay, results = optimize_chain()
    
    # print final results
    print('\nBest values were:')
    print(f'\tfan = {best_config[1]}')
    print(f'\tnum_inverters = {best_config[0]}')
    print(f'\ttphl = {best_delay}')

    # write results to file
    write_results_to_file(best_config, best_delay, results)

if __name__ == "__main__":
    main()