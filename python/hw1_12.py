from math import sqrt

prime_list = [2] #Manually move 2 into the prime_list

for n in range(3,10001): #Check the numbers from 3 to 10000
    is_prime = True #I give all the numbers ture at first, then if it isn't prime number I will turn to False in the end
    for prime in prime_list: 
        if prime > sqrt(n): # Go through all the number in the prime list comparing numerical values
            break
        if n % prime == 0: # The number which can be divided by a value in the prime list trun False
            is_prime = False
            break
    if is_prime:
        prime_list.append(n) #Use append to put number into prime_list
print(prime_list)
        




        