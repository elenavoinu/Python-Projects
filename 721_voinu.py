#Elena Voinu
#Create a conditional expression that evaluates to string "negative" if user_val is less than 0, 
#and "non-negative" otherwise. Example output when user_val is -9 
#sample program: -9 is negative


user_val = -9
#''' Your solution goes here '''

cond_str = "negative"  if user_val < 0 else  "non-negative"

print(user_val, 'is', cond_str)
