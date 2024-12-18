# example illustrating the binary search method
# author sdm

# consider x^2 + 2x + 1 = 0, which factors into (x+1)(x+1)=0
# rewrite as x = -(x^2 + 1)/2

START_VALS = [2,.5]        # pick some starting values
TOO_BIG    = -1e35         # if answer gets bigger than this, stop!
ITERATIONS = 20000         # maximum number of iterations
REPORT_ALL = 5             # report all values for first few iterations
REPORT_MOD = 3000          # then report only occasionally

################################################################################
# Compute a new value of x for the relaxation method                           #
# input: x_in, the current value of x                                          #
# output: the new value of x                                                   #
################################################################################

def relax(x_in):
    return -((x_in * x_in) + 1)/2

# keep iterating from the start value until done
for x in START_VALS:
    print("Starting value",x)
    error = 0
    for iter in range(ITERATIONS):
        x = relax(x)
        if ( iter < REPORT_ALL ) or ( iter % REPORT_MOD == 0 ):
            print(iter,":",x)
        if x < TOO_BIG:
            print(iter,":",x,"Not Converging!")
            error = 1
            break;
    if not error:
        print("Final value after",ITERATIONS,"iterations",x,"\n")
    else:
        print("")
