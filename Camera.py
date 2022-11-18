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

    def startRecording(self):
        print("Start Recording")

    def stopRecording(self):
        print("Stop Recording")

    def focusIn(self):
        print("Adjust focus (In)")

    def focusOut(self):
        print("Adjust focus (Out)")