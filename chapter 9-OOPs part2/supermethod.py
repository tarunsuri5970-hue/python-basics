class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("car is start")
    @staticmethod
    def stop():
        print("car is stop")

class toyotaCar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
car1 = toyotaCar("fortuner","electrical")


print(car1.type)