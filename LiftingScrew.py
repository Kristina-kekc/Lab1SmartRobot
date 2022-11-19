class LiftingScrew:
    def __init___(self,size):
        self.size = size
    
    def LiftUp(self):
        print ("Lifting up")

    def LiftDown(self):
        print("Lifting down")

    def adjustHeight(self, level):
        self._level = level
        print(f"Adjust lifting hight to {level}")
        