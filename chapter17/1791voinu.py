# Elena Voinu

class CarRecord:
    def __init__(self):
        self.year_made = 0
        self.car_vin = ''

    # FIXME add __str__()

    ''' Your solution goes here '''
    def __str__(self):
        return "Year: "+str(self.year_made)+", VIN: "+str(self.car_vin)


my_car = CarRecord()
my_car.year_made = 2009
my_car.car_vin = 'ABC321'

print(my_car)