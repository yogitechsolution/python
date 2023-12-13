# Class - In class we define all the functions and methods which belongs to 1 class.
# Pascal naming convention : We use for naming classes.
# e.g. Point, EmailClient, etc etc

# In the class we define 2 new type, in this new type we can create new OBJECTS
#An OBJECT is an instance of a class, a CLASS simply defines the blueprint OR the template for creating OBJECTS
#And the OBJECTS are the actual instances based on the blueprint

class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

#To create object

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x) #10
point1.draw() #draw
