#Elena Voinu

country_capital = {'Spain': 'Madrid', 'Togo': 'Lome', 'Prussia': 'Konigsberg'}

''' Your solution goes here '''

del country_capital['Prussia']

print('Prussia deleted?', end=' ')

if 'Prussia' in country_capital:
    print('No.')
    
else:
    print('Yes.')