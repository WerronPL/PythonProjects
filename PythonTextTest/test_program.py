
import functions

Vehicle = functions.VehicleClass
Start = functions.StartClass
Amogus = functions.AmogusClass
self = functions.VehicleClass.__init__


class Car(Vehicle):
    Vehicle.open_trunk(self)

class Motorcycle(Vehicle):
    Start.start_car(self)
    

class Imposter(Amogus):
    Amogus = functions.AmogusClass.who_is_sus(self)
    