#Define a function pyramid_volume with parameters base_length, base_width, 
#and pyramid_height, that returns the volume of a pyramid with a rectangular base. 

#Relevant geometry equations: 
#Volume = base area x height x 1/3 
#Base area = base length x base width. 

#''' Your solution goes here '''
def pyramid_volume(base_length, base_width, pyramid_height):
 
    pyramid_volume = base_length * base_width* pyramid_height * (1 / 3)
    
    return pyramid_volume

print('Volume for 4.5, 2.1, 3.0 is:', pyramid_volume(4.5, 2.1, 3.0))