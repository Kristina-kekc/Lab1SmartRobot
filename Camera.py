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

    def record(self):
        print("Start Recording")

    def focus(self):
        print("Adjust focus")

    def transferInput(self):
        print("Transfer recording")