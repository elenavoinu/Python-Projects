''' Elena Voinu
Write nested loops to print a rectangle. Sample output for given program:
* * *  
* * * 
'''

num_rows = 2
num_cols = 3

''' Your solution goes here '''
for i in range(num_rows):
    print('*', end=' ')
    for j in range(num_cols-1):
        i*=j

        print('*', end=' ')
    print()