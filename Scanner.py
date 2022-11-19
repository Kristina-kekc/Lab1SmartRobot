"""
File containing Scanner class
"""
class Scanner:
    def __init__(self, type) -> None:
       self._type = type

    def On(self):
        print ("Scanner is on")

    def Off(self):
        print ("Scanner is off")

    def continiousScan(self):
        print ("Scanner is on and scanning bar codes continiously")

    def adjust(self):
        print ("Scaner adjustment")