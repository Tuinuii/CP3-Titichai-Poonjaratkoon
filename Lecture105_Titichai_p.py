class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn In : Air")

class Car(Vehicle):
    pass
class PickUp(Vehicle):
    pass
class Van(Vehicle):
    pass
class EstateCar(Vehicle):
    pass

car1 = Car()
car1.turnOnAirConditioner()

car2 = PickUp()
car2.turnOnAirConditioner()

car3 = Van()
car3.turnOnAirConditioner()

car4 = EstateCar()
car4.turnOnAirConditioner()
