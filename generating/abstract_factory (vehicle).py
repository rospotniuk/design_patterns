class Vehicle:
    def __init__(self, vehicle_factory=None):
        self.vehicle = vehicle_factory
        self.__go = False             # The vehicle rides or isn't moving

    def start(self):
        self.__go = True
    def stop(self):
        self.__go = False

    def __str__(self):
        go = 'rides' if self.__go else 'is not moving'
        return '{} {}'.format(self.vehicle.type, go)
    def view(self):
        wheels = self.vehicle.set_wheels()
        doors = self.vehicle.set_doors()
        seats = self.vehicle.set_seats()
        print('The vehicle "{}" consists of {} wheels with size {}, {} doors and {} seats'.\
              format(self.vehicle.type, wheels.amount, wheels.size, doors.amount, seats.amount))

    # Base classes
class Wheels:
    """Wheels, their amount and size"""
    size = None
    amount = None

class Doors:
    """Doors and their amount"""
    amount = None

class Seats:
    """Seat and their amount"""
    amount = None

    # Abstract Factory
class AbstractFactory:
    def set_doors(self):
        pass
    def set_seats(self):
        pass
    def set_wheels(self):
        pass

    # Concrete Factory 1
class CarFactory(AbstractFactory):
    type = "Car"
    def set_doors(self):
        doors = Doors()
        doors.amount = 4
        return doors
    def set_seats(self):
        seats = Seats()
        seats.amount = 5
        return seats
    def set_wheels(self):
        wheels = Wheels()
        wheels.size = 16
        wheels.amount = 4
        return wheels

    # Concrete Factory 1
class BikeFactory(AbstractFactory):
    type = "Bike"
    def set_doors(self):
        doors = Doors()
        doors.amount = 0
        return doors
    def set_seats(self):
        seats = Seats()
        seats.amount = 2
        return seats
    def set_wheels(self):
        wheels = Wheels()
        wheels.size = 14
        wheels.amount = 2
        return wheels

#===========================================================
if __name__ == "__main__":

    car = Vehicle(CarFactory())
    car.view()
    car.start()
    print(car)
    car.stop()
    print(car)

    bike = Vehicle(BikeFactory())
    bike.view()
    bike.start()
    print(bike)

