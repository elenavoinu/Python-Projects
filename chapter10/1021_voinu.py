#Elena Voinu
#10.2.1: Function with branch: Popcorn.

''' Your solution goes here '''
def print_popcorn_time(bag_ounces):
    
    if bag_ounces < 3:
        print("Too small")
        
    elif bag_ounces > 10:
        print("Too large")
        
    else:
        print( 6 * bag_ounces, end=' ')
        print("seconds")
        
print_popcorn_time(7)