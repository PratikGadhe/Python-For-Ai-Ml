class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class toyato(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name

car1=toyato("Fortuner","diesel")
print(car1.type)