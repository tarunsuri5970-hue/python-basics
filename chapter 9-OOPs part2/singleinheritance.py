class car:
    @staticmethod
    def start():
        print("car is start")
    @staticmethod
    def stop():
        print("car is stop")

class toyotaCar(car):
    def __init__(self,name):
        self.name=name

car1 = toyotaCar("fortuner")
car2 = toyotaCar("maruti")

print(car1.start())