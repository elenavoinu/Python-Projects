#@evoinu
#Using the celsius_to_kelvin function as a guide, create a new function, 
#changing the name to kelvin_to_celsius, and modifying the function accordingly.

def celsius_to_kelvin(value_celsius):
    value_kelvin = 0.0

    value_kelvin = value_celsius + 273.15
    return value_kelvin

#''' Your solution goes here '''
def kelvin_to_celsius(value_k):
    value_celsius = 0.0

    value_celsius = value_k - 273.15
    return value_celsius

value_c = 0.0
value_k = 0.0

value_c = 10.0
print(value_c, 'C is', celsius_to_kelvin(value_c), 'K')

value_k = 283.15
print(value_k, 'K is', kelvin_to_celsius(value_k), 'C')
