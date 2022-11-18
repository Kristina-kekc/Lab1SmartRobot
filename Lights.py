"""
 File containing Lights class
"""
class Lights:
    def __init__(self,color) -> None:
      self._color = color

    def Light(self, color):
        print ("Choose light color {color}")

    def On(self):
        print("Turn lights on")

    def Off(self):
        print("Turn lights off")

    def flashing(self):
        print("Lights are flashing")