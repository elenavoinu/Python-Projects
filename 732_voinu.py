#Elena Voinu
#Write an expression that will print "Dollar or more" if the value of num_cents is
#at least a dollar (100 cents is a dollar). 
#Ex: If num_cents is 109, output is "Dollar or more". 


num_cents = 109

# ''' Your solution goes here ''':
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')