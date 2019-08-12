''' Elena Voinu
Given num_rows and num_cols, print a list of all seats in a theater. 
Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat, 
including after the last. Ex: num_rows = 2 and num_cols = 3 prints:
1A 1B 1C 2A 2B 2C 
'''


num_rows = 2
num_cols = 3

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

''' Your solution goes here '''
val = 65
s = " "
for i in range(1, num_rows+1):
    val = 65
    for j in range(1, num_cols+1):
        s = str(i) + chr(val)
        print(s, end = ' ')
        val = val + 1