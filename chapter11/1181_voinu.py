#Elena Voinu

mult_table = [
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
]

''' Your solution goes here '''

for i in range(0,len(mult_table)):
    
    for j in range(0,len(mult_table[i])):
        
        print (mult_table[i][j],end='')
        
        if j!=len(mult_table)-1 :
            
            print(end=" | ")
            
    print()