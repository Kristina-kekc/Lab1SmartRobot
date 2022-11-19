class Speaker:
    def __init__(self, volume, tone):
        self._volume = volume
        self._tone = tone

    def play(self):
        print ("Start playing sound")

    def stop(self):
        print ("Stop playing sound")

    def setVolume(self, volume):
        print (f"Set volume to {volume}")

    def setTone(self, tone):
        print (f"Set tone to {tone}")