"""
 File containing Wheels class
"""
class Wheels:
    def __init__(self,diameter) -> None:
      self._diameter = diameter

    def Left(self):
        print("Turn wheels left")

    def Right(self):
        print("Turn wheels right")
    
    def spin360(self):
        print("Turn wheels 360 degrees")

    def Forward(self):
        print("Move forward")

    def Backwards(self):
        print("Move backwards")
    

