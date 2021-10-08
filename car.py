class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.color=color
        self.model=model
        self.company=company
        self.speedLimit=speedLimit
    def start(self):
        print("Car Has Started")
    def stop(self):
        print("Car Has Stoped")
    def accelerate(self):
        print("Car Is Accelerating")
    def changeGear(self,gear_type):
        print("Gear Has Changed")

Supra=Car("Toyota Gt","Black","Toyota","280Km/h")
Mercedes=Car("X5","White","Mercedes","230Km/h")

print(Supra.start())
print(Mercedes.stop())
print(Mercedes.model)


        