"""
 File containing Lights class
"""
class Lights:
    def __init__(self):
        print("Lights")
        
    def On(self):
        print("Turn lights on")

    def Off(self):
        print("Turn lights off")

    def flashing(self):
        print("Lights are flashing")
    
    def singleOn(self, lightno):
        print(f"Only #{lightno} light is on")
        for i in range(0,len(self._lights)):
            if i == lightno:
                self._lights[i].on()
            else:
                self._lights[i].off()
    
class LightColor(Lights):

    def __init__(self, green, yellow, red):
        print("Light colors - green,yellow,red")
        super().__init__()
        self._lights.append(green)
        self._lights.append(yellow)
        self._lights.append(red)
    
    def green(self):
        print("Light is Green")
        self.singleOn(0)
    
    def yellow(self):
        print("Light is yellow")
        self.singleOn(1)

    def red(self):
        print("Light is red")
        self.singleOn(2)