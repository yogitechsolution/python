class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    def bark(self):
        print("bark")


class Cat(Animal):
    def cute(self): #Defined 1 method in our Cat class
        print("cute")


dog1 = Dog()
dog1.bark() 
cat1 = Cat()
cat1.cute() #Can get 2 methods to call, since 1 is inherited

#o/p
#bark
#cute