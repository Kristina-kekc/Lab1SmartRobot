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
from Model import *

class Robot:

 def buildModel(self):

    self._model = Model(4, self)

    self._model.addTransition(1, TIMEOUT, 2)
    self._model.addTransition(2, TIMEOUT, 3)
    self._model.addTransition(3, TIMEOUT, 0)

def stateEntered(self, stateno):
    if stateno == 0:
        self._Engine.off()
        self._Lights.off()
        self._break.apply()
        self._Camera.stopRecording()
        self._ImageSensor.Off()
        self._Scanner.Off()
    
    elif stateno == 1:
        self._Break.release()
        self._Lights.on()
        self._Engine.On()
        self._Speaker.setVolume(5)
        self._Speaker.play()
        self._TaskManager.SendTask()
        self._Camera.On()
        self._ImageSensor.On()
        self._Scanner.On()
        self._LightColor.green()
    
    elif stateno == 2:
        self._Engine.startMoving()
        self._Wheels.forward()
        self._Lights.flash()
        self._Camera.StartRecording()
    
    elif stateno == 3:
        self._Breaks.apply()
        self._Wheels.right()
        self._LightColor.red()
    else:
        print("Invalid state")


    def stateLeft(self, stateno):
        if stateno == 1:
            print ("Exiting State 1")
        elif stateno == 2:
            self._Robot.ValidateTask()
            self._Speaker.off()
        elif stateno == 3:
            self._Wheels.Left
        else:
            pass


    def run(self):
        self.model.start()
        while self._model._running:
            if self._model._curState == 0:
                if self._TaskManager.sendTask():
                    self._model.gotoState(1)
            if self._model._curState == 1:
                self._ImageSensor.monitor()
                self._Scanner.continiousScan()
            if self._model._curState == 2:
               if self._ImageSensor.obstacle():
                    self._model.gotoState(3)
            if self._model._curState == 3:
                self._Wheels.forward(2)

            else:
                pass





    def __init__(self, serialNum, year, model) -> None:
        self._serialNum = serialNum # self. makes it an attribute
        self._year = year
        self._model = model
        
  #  def Main(self):
  #      print ("Stop robot movement")

  #  def systemCheck(self):
   #     print("Full System Check")

if __name__ == "__Robot__":
    m = Robot()
    m.run()
