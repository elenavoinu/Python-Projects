#Assign max_sum with the max of (num_a, num_b) PLUS the max of (num_y, num_z). 
#Use just one statement. Hint: Call find_max() twice in an expression. 

def find_max(num_1, num_2):
   max_val = 0.0

   if (num_1 > num_2):  # if num1 is greater than num2,
      max_val = num_1   # then num1 is the maxVal.
   else:                # Otherwise,
      max_val = num_2   # num2 is the maxVal
   return max_val

num_a = 5.0
num_b = 10.0
num_y = 3.0
num_z = 7.0
max_sum = 0.0

#''' Your solution goes here '''
max_sum = find_max(num_a, num_b) + find_max(num_y, num_z)

#just testing if it works, not in the book
print(max_sum)

