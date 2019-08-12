# author Elena Voinu

''' Your solution goes here '''
class PatientData:
    height_inches = 0
    weight_pounds= 0

lunaLovegood = PatientData()
print('Patient data (before):', end=' ')
print(lunaLovegood.height_inches, 'in,', end=' ')
print(lunaLovegood.weight_pounds, 'lbs')


lunaLovegood.height_inches = 63
lunaLovegood.weight_pounds = 115

print('Patient data (after):', end=' ')
print(lunaLovegood.height_inches, 'in,', end=' ')
print(lunaLovegood.weight_pounds, 'lbs')