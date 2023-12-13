# define new type - Person, this object has 2 attributes - person and talk() method

class Person:
    def talk(self):
        print("talk")


#yogi = Person()
#yogi.talk() 

#o/p 
#talk

#Adding constructer fun to add a person name
class Person:
    def __init__(self, name): ##Self is reference to the currect object e.g. line 22 calling function
        self.name = name  ##.name is an attribute and name is an argument
    def talk(self):
        print("talk")


yogi = Person("Yogi Sri")
#print(yogi.name)
#yogi.talk() 

#o/p 
#Yogi Sri
# talk

# Instead of printing boring msg as "talk", print good msg e.g. Hi I am Yogi
class Person:
    def __init__(self, name): 
        self.name = name  
    def talk(self):
        print(f"Hi I am {self.name}") # changed here


yogi = Person("Yogi Sri")
yogi.talk() 
john = Person ("John Smith")
john.talk()

#o/p 
# Hi I am Yogi Sri
# Hi I am John Smith

# Note: Each object is a different instance of a Person class
