"""
File containing Camera class
"""
class Camera:
    def __init__(self, mode, setting, focus, lens) -> None:
        self._mode = mode
        self._setting = setting
        self._focus = focus
        self._lens = lens

    def setMode(self):
        print("Set camera mode")

    def focusIn(self):
        print("Adjust focus (In)")

    def focusOut(self):
        print("Adjust focus (Out)")

    def startRecording(self):
        print("Start Recording")

    def stopRecording(self):
        print("Stop Recording")

class ImageSensor(Camera):

    def __init__(self, type, input):
        print ("Image Sensor constructor")
        super().__init__()
        self._append(type)
        self._append(input)

       
def Off(self):
    print("Turn on sensor")

def On(self):
    print ("Turn off the sensor")

def adjust(self):
    print("Adjust the sensor")

def sendInput(self):
    print("Send input from the sensor")

def monitor(self):
    print("Monitor the surroundings")

class Flash(Camera):
    def __init__(self, setting):
        super().__innit__()
        self.append(setting)

    def on(self):
        print("Flash is on")

    def off(self):
        print("Flash is off")

class Lens(Camera):
    def __init__(self, zoom, focus):
        super().__init__()
        self._append(zoom)
        self._append(focus)

    def zoomIn(self):
        print("Zoom In")

    def zoomOut(self):
        print("Zoom Out")