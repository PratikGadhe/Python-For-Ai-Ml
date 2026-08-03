# When one class(child/derived) derives the properties & methods of another class(parentlbase).
class car:
    @staticmethod
    def start():
        print("Car Started..")
    @staticmethod
    def stop():
        print("Car Stopped..")
class toyoto_car(car):
    def __init__(self,name):
        self.name=name
car1=toyoto_car("Fortuner")
print(car1.start())