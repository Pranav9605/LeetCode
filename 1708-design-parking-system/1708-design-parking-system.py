class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big=big
        self.med=medium
        self.small=small
    def addCar(self, carType: int) -> bool:
        if carType==1:
            if self.big>0:
                self.big-=1
                return True
        if carType==2:
            if self.med>0:
                self.med-=1
                return True
        if carType==3:
            if self.small>0:
                self.small-=1
                return True
        return False
            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)