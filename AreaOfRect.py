class Rect():
    def __init__(self, l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l*self.b
    


length = int(input("Enter length : "))
breath = int(input("Enter breath : "))
NewRect= Rect(length, breath)
print(NewRect.area())
