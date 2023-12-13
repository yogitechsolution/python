# Constructor - used to construct or create an object e.g. by initialising it


class Point:
    def __init__(self, x, y): #Self is reference to the currect object e.g. line 17 calling function
        self.x = x  #.x is an attribute and x is an argument
        self.y = y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

#To create object

point = Point(10, 20)
point.x = 11 # Can update the value
print(point.x) #10