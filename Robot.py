"""
This is Kiva Robot 
"""


from Breaks import *
from Camera import *
from Engine import *
from LiftingScrew import *
from Lights import *
from Scanner import *
from Speaker import *
from TaskManager import *
from Wheels import *
 
class Robot:

    def __init__(self, serialNum, year, model) -> None:
        self._serialNum = serialNum # self. makes it an attribute
        self._year = year
        self._model = model
        


    def Main(self):
        print ("Stop robot movement")

    def systemCheck(self):
        print("Full System Check")
