# Elena Voinu

# Returns number of pennies if pennies are doubled num_days times
def double_pennies(num_pennies, num_days):
    total_pennies = 0
    
    ''' Your solution goes here '''

    if num_pennies == 0:
        return 0

    elif num_days == 0:
        return total_pennies + num_pennies

    else:
        total_pennies = double_pennies((num_pennies * 2), (num_days - 1))

    return total_pennies

# Program computes pennies if you have 1 penny today,
# 2 pennies after one day, 4 after two days, and so on
starting_pennies = int(input("Enter pennies: "))
user_days = int(input("Enter days: "))

print('Number of pennies after', user_days, 'days: ', end="")
print(double_pennies(starting_pennies, user_days))