# Elena Voinu

test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

''' Your solution goes here '''
sum_extra = sum([grade - 100 for grade in test_grades if grade > 100])
print('Sum extra:', sum_extra)