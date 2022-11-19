class Breaks:
    def __init__(self, type, level) -> None:
        self._type = type
        self._level = level

    def apply(self):
        print ("Apply Breaks")

    def release(self):
        print ("Release breaks")

    def adjust(self, level):
        print(f"Adjust breaks to {level}")