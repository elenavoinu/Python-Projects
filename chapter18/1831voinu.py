# Elena Voinu
'''function number_of_pennies() that returns the total number
   of pennies given a number of dollars and (optionally) a number of pennies. 
   Ex: 5 dollars and 6 pennies returns 506. 
'''

''' Your solution goes here '''
def number_of_pennies(dollar=0,pennies=0):
    
    #declare variable total is 0
    total_pennies = 0

    #compute total pennies
    total_pennies=100*dollar+pennies


    return total_pennies

print(number_of_pennies(5, 6)) # Should print 506
print(number_of_pennies(4))    # Should print 400