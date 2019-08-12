# Fix the indentation as necessary to make the program work.
# @evoinu

temperatures = {
    'Seattle': 56.5,
    'New York': 105,
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

#''' Your solution goes here '''
if 'New York' in temperatures:
    
    if temperatures['New York'] > 90:
        print('The city is melting!')
        
    else:
        print('The temperature in New York is', temperatures['New York'])
        
else:
    print('The temperature in New York is unknown.')
