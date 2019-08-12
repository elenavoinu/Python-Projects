#Elena Voinu
#Write multiple if statements. If car_year is 1969 or earlier, print "Few safety features.". 
#If 1970 or later, print "Probably has seat belts.". 
#If 1990 or later, print "Probably has antilock brakes.". 
#If 2000 or later, print "Probably has airbags." 
#End each phrase with a period and a newline. 
#Ex: car_year = 1995 prints:
                #Probably has seat belts.
                #Probably has antilock brakes.

car_year = 1964

#''' Your solution goes here '''

if car_year <= 1969:
    print("Few safety features.")
elif car_year >= 1970:
    print("Probably has seat belts.")
    if car_year >= 1990:
        print("Probably has antilock brakes.")
if car_year >= 2000:
    print("Probably has airbags.")
