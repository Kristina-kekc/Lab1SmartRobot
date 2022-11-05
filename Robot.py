"""
This is Kiva Robot 
"""
class Robot:

    def __init__(self, serialNum, year) -> None:
        self._serialNum = serialNum # self. makes it an attribute
        self._year = year
        

    def moveForward(self):
        print("Move robot forward")

    def moveBackward(self):
        print ("Move robot backward")

    def stop(self):
        print ("Stop robot movement")

    def systemCheck(self):
        print("Full System Check")
