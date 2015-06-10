import copy

    # Prototype
class Prototype(object):
    def __init__(self):
        self._objects = {}
    def register_object(self, name, object):   # Register an object
        self._objects[name] = object
    def unregister_object(self, name):      # Unregister an object
        del self._objects[name]
    def clone(self, name, **attr):          # Clone a registered object and update inner attributes dictionary
        object = copy.deepcopy(self._objects.get(name))
        object.__dict__.update(attr)
        return object

class Vehicle:
    def __init__(self):
        self.type = None
        self.go = False             # The vehicle rides or isn't moving
        self.wheels = 0
        self.doors = 0
        self.seats = 0

    def start(self):
        self.go = True
    def stop(self):
        self.go = False

    def __str__(self):
        go = 'rides' if self.go else 'is not moving'
        return '{} {}'.format(self.type, go)

    def view(self):
        print('The vehicle "{}" consists of {} wheels, {} doors and {} seats'.\
              format(self.type, self.wheels, self.doors, self.seats))

#===========================================================
if __name__ == "__main__":

    vehicle = Vehicle()
    prototype = Prototype()
    prototype.register_object('empty', vehicle)
    empty_2 = prototype.clone('empty')
    car = prototype.clone('empty', type="Car", wheels=4, doors=4, seats=5)
    bike = prototype.clone('empty', type="Bike", wheels=2, seats=2)

    vehicle.view()
    print(vehicle)

    empty_2.view()
    print(empty_2)

    car.view()
    print(car)
    car.start()
    print(car)
    car.stop()
    print(car)

    bike.view()
    bike.start()
    print(bike)

    end = prototype.unregister_object('empty')
    #end.view()     # AttributeError: 'NoneType' object has no attribute 'view'

