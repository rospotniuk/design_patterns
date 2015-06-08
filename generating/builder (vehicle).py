    # Product
class Vehicle:
    def __init__(self, vehicle_type):
        self.type = vehicle_type
        self.__go = False             # The vehicle rides or isn't moving
        self.__wheels = None
        self.__doors = None
        self.__seats = None

    def set_wheels(self, wheels):
        self.__wheels = wheels
    def set_doors(self, doors):
        self.__doors = doors
    def set_seats(self, seats):
        self.__seats = seats

    def start(self):
        self.__go = True
    def stop(self):
        self.__go = False

    def __str__(self):
        go = 'rides' if self.__go else 'is not moving'
        return '{} {}'.format(self.type, go)
    def view(self):
        print('The vehicle "{}" consists of {} wheels with size {}, {} doors and {} seats'.\
              format(self.type, self.__wheels.amount, self.__wheels.size, self.__doors.amount, self.__seats.amount))

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

    # Director
class VehicleManufacturer:

    def __init__(self):
        self.builder = None
    def construct_vehicle(self, type):
        assert not self.builder is None, "No defined builder"
        vehicle = Vehicle(type)

        doors = self.builder.get_doors()
        vehicle.set_doors(doors)

        seats = self.builder.get_seats()
        vehicle.set_seats(seats)

        wheels = self.builder.get_wheels()
        vehicle.set_wheels(wheels)
        return vehicle

    # Abstract Builder
class VehicleBuilder:
    def get_doors(self):
        pass
    def get_seats(self):
        pass
    def get_wheels(self):
        pass

    # Concrete Builder 1
class CarBuilder(VehicleBuilder):
    def get_doors(self):
        doors = Doors()
        doors.amount = 4
        return doors
    def get_seats(self):
        seats = Seats()
        seats.amount = 5
        return seats
    def get_wheels(self):
        wheels = Wheels()
        wheels.size = 16
        wheels.amount = 4
        return wheels

    # Concrete Builder 2
class BikeBuilder(VehicleBuilder):
    def get_doors(self):
        doors = Doors()
        doors.amount = 0
        return doors
    def get_seats(self):
        seats = Seats()
        seats.amount = 2
        return seats
    def get_wheels(self):
        wheels = Wheels()
        wheels.size = 14
        wheels.amount = 2
        return wheels

    # Client
if __name__ == "__main__":
    manufacturer = VehicleManufacturer()

    manufacturer.builder = CarBuilder()
    car = manufacturer.construct_vehicle("Car")
    car.view()
    car.start()
    print(car)
    car.stop()
    print(car)

    manufacturer.builder = BikeBuilder()
    bike = manufacturer.construct_vehicle("Bike")
    bike.view()
    bike.start()
    print(bike)

