# Elena Voinu

hourly_temperature = [90, 92, 94, 95]

''' Your solution goes here '''
# calculate the length of the list
length = len(hourly_temperature)


for i in range(length):
    # For the last element or if there is only one element
    if i==length-1:
        print(hourly_temperature[i]," ", sep='')
  # use separator sep=' ' between the arguments for spaces around the arrows
    else:
        print(hourly_temperature[i]," -> ",sep='',end='')
  