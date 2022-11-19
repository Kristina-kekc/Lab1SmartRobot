"""
 File containing Engine class
"""
class Engine:
    def __init__(self, speed) -> None:
        self._speed = speed 


    def On(self):
        print ("Start Engine")

    def Off(self):
        print("Stop Engine")

    def startMoving(self):
        print ("Robot starts moving")

    def stopMoving(self):
        print ("Robot starts moving")