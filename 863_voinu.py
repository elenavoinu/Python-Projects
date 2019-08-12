''' Elena Voinu
Given positive integer num_insects, write a while loop 
that prints that number doubled up to, but without exceeding 100.
Follow each number with a space. '''


num_insects = 8 # Must be >= 1

''' Your solution goes here '''

while num_insects <= 100:        
  print(num_insects,'', end="")
  num_insects = num_insects * 2
