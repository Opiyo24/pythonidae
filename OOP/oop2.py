class Toyota:
    def __init__(self, name, year):
        self.name = name
        self.year = year

car_1 = Toyota("Corolla", 2012)
car_2 = Toyota("Land cruiser", 2018)
car_3 = Toyota("Lexus", 2011)

print("Car 1 is a Toyota {} make year {}".format(car_1.name, car_1.year))
print("Car 2 is a Toyota {} make year {}".format(car_2.name, car_2.year))
print("Car 3 is a Toyota {} make year {}".format(car_3.name, car_3.year))