# Example to find maximum efficiency temp of light bulb
# author: olhartin@asu.edu updated by sdm

################################################################################
# Function to implement the golden search                                      #
# Inputs:                                                                      #
#    func - the function for which a max is desired                            #
#    x1,x2,x3,x4 - the current values, lowest to largest                       #
#    tol         - the tolerance: quit if x1 and x4 are closer than tol        #
# Outputs:                                                                     #
#    x1,x2,x3,x4 - the new values, lowest to largest                           #
################################################################################

def goldsearch(func,x1,x2,x3,x4,tol):
    if (x4-x1>tol):                                         # not close yet?
        if (max(func(x2),func(x3))>max(func(x1),func(x4))): # a middle > outside
            if (func(x2)>func(x3)):   # if x2 is bigger than x3...
                x4 = x3                   # slide x4 down to x3
                x3 = x2                   # slide x3 down to x2
                x2 = (x1+x3)/2.0          # x2 is average of x1 and old x2
            else:                     # if x3 was bigger than x2...
                x1 = x2                   # slide x1 up to x2
                x2 = x3                   # slide x2 up to x3
                x3 = (x2+x4)/2.0          # x3 is average of x4 and old x3

            # either way, we search again with the new values
            x1,x2,x3,x4 = goldsearch(func,x1,x2,x3,x4,tol)

        #else:  # the max is outside the range of x2:x3 same as at x1 or x4
            #print(x1,x2,x3,x4,func(x1),func(x2),func(x3),func(x4))

    #else:  # we're close enough...
        #print(x1,x2,x3,x4,func(x1),func(x2),func(x3),func(x4))

    return(x1,x2,x3,x4)
