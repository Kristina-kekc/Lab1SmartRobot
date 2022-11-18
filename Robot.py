"""
This is Kiva Robot 
"""
class Robot:

    def __init__(self, serialNum, year, model) -> None:
        self._serialNum = serialNum # self. makes it an attribute
        self._year = year
        self._model = model
        


    def Main(self):
        print ("Stop robot movement")

    def systemCheck(self):
        print("Full System Check")
