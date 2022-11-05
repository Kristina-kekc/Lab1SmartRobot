"""
 File containing Lights class
"""
class Lights:
    def __init__(self,color) -> None:
      self._color = color

    def turnOn(self):
        print("Turn lights on")

    def turnOff(self):
        print("Turn lights off")

    def flashing(self):
        print("Lights are flashing")