class car:
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class toyoto_car(car):
    def __init__(self,brand):
        self.brand=brand
class fortuner(toyoto_car):
    def __init__(self, type):
        self.type=type

car1=fortuner("Diesel")
car1.start()