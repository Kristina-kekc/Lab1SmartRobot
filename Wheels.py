"""
 File containing Wheels class
"""
class Wheels:
    def __init__(self,diameter) -> None:
      self._diameter = diameter

    def turnLeft(self):
        print("Turn wheels left")

    def turnRight(self):
        print("Turn wheels right")
    
    def spin360(self):
        print("Turn wheels 360 degrees")

    def rise(self, distance):
        print(f"Rise wheels {distance} inches")
        self._rise = distance

    def drop(self, distance):
        print(f"Drop wheels {distance} inches")
        self._drop = distance 

