from car import Car
class ElectricCar (Car):
    def __init__(self,color, mile, typ):
        super().__init__(color, mile, typ)

    def getCarType (self):
          print ("The type of car is: "+self.type)

myElectricCar = ElectricCar("yellow",220, "Electric") 
myElectricCar.getCarType()
myElectricCar.getCarColour()