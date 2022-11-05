"""
File containing Scanner class
"""
class Scanner:
    def __init__(self, type, input) -> None:
       self._type = type
       self._input = input

    def scan(self):
        print ("Scan barcode)")