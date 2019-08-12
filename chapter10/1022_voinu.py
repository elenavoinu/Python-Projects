#Elena Voinu
#10.2.2: Function with loop: Shampoo

''' Your solution goes here '''
def shampoo_instructions(num_cycles):
    
    if num_cycles < 1:
        print("Too few.")
        
    elif num_cycles > 4:
        print ("Too many.")
        
    else:
        for i in range(num_cycles):
            print(i+1,': Lather and rinse.')
            
        print("Done.")
        
shampoo_instructions(2)