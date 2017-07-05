class RaceCar:

    # attributes set here would be universal

    def __init__(self, color, fuel_remaining, laps=0, **kwargs): # defines attributes explicitly for instances
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = laps

        for key, value in kwargs.items():
            setattr(self, key, value)

    def run_lap(self, length):
        self.fuel_remaining = self.fuel_remaining - (length * 0.125)
        self.laps += 1
        return self.fuel_remaining


'''In Python, attributes defined on the class, but not an instance, are universal. So if you change the value of the attribute, any instance 
that doesn't have it set explicitly will have its value changed, too!  For example, right now, if we made a RaceCar instance named red_car, then 
did RaceCar.laps = 10, red_car.laps would be 10!  To prevent this, be sure to set the laps attribute inside of the __init__ method (
it doesn't have to be a keyword argument, though)'''

'''Attributes set outside the init method are universal.  For example if I had a laps attribute set to 20 and changed it
to 22 (RaceCar.laps = 22), any instance created afterwards would have laps set to 22.  '''