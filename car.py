class Car():
    def __init__(self, color, mile, typ):
        self.colour = color
        self.mileage = mile
        self.type = typ

    def getCarColour (self):
        print("The colour of the car is: "+self.colour.title())
        
    def getCarMileage (self):
        print ("The milage of this car is: %d "%self.mileage)
    
    def getCarType (self):
        print ("The type of card is: "+self.type)

