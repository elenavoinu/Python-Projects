#Write an expression using Boolean operators that prints "Eligible"
#if user_age is greater than 17 and not equal to 25. 
#Ex: 17 prints "Ineligible", 18 prints "Eligible". 

user_age = 17

#''' Your solution goes here '''
if (user_age > 17) and (user_age != 25):
    print('Eligible')
else:
    print('Ineligible')