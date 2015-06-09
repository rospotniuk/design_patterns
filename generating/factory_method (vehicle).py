    # Product
class Vehicle(object):
    __go = False             # The vehicle rides or isn't moving

    def __init__(self):
        self._type = None
        self._wheels = None
        self._doors = None
        self._seats = None

    def get_doors(self):
        return self._doors
    def get_seats(self):
        return self._seats
    def get_wheels(self):
        return self._wheels

    def start(self):
        self.__go = True
    def stop(self):
        self.__go = False

    def __str__(self):
        go = 'rides' if self.__go else 'is not moving'
        return '{} {}'.format(self._type, go)
    def view(self):
        print('The vehicle "{}" consists of {} wheels, {} doors and {} seats'.\
              format(self._type, self._wheels, self._doors, self._seats))

    # Concrete Product 1
class Car(Vehicle):
    def __init__(self):
        self._type = "Car"
        self._wheels = 4
        self._doors = 4
        self._seats = 5

    # Concrete Factory 1
class Bike(Vehicle):
    def __init__(self):
        self._type = "Bike"
        self._wheels = 2
        self._doors = 0
        self._seats = 2

class VehicleFactory(object):
    @classmethod
    def construct_vehicle(self, type):
        if type == "Car":
            return Car()
        elif type == "Bike":
            return Bike()

#===========================================================
if __name__ == "__main__":

    car = VehicleFactory.construct_vehicle("Car")
    car.view()
    print(car)
    car.start()
    print(car)
    car.stop()
    print(car)

    bike = VehicleFactory.construct_vehicle("Bike")
    bike.view()
    print(bike)
    bike.start()
    print(bike)

