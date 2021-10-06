###################################
# This scirpt is used to calculate the prime Factors for the given number
# Author: 
# Created at: 24/09/2021
# Last Modified at: 24/09/2021
#################################

from math import ceil, remainder, floor



def check_for_prime(x):
    flag = True   #if the flag is True then it has factors
    for i in range(2, x):
        if (x % i) == 0:
            flag = False
            break
    
    return flag

def check_remainder(list1, y):
    for item in list1:
        if (y % item) == 0:
            break
    return item

def PrimeFactors(get_primefactor):
    the_number = get_primefactor
    lowest_prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        if check_for_prime(the_number):
            print(the_number)
            break
        else:
            choosen_number = check_remainder(lowest_prime_numbers, the_number)
            print(choosen_number)
            remainder_number = ceil(the_number/choosen_number)
            the_number = remainder_number



get_primefactor = int(input("Enter the number to get Prime factor: "))

PrimeFactors(get_primefactor)


