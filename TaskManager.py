class TaskManager:
    def __init__(self, name, mode) -> None:
        self._name = name
        self._mode = mode

    def receiveTask(self):
        print ("Task received")
    
    def sendTask(self):
        print ("Taks sent")

    def systemCheck(self):
        print ("System Check")

