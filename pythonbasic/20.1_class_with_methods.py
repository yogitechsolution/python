class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    def bark(self): #Defined 1 method in our Dog class
        print("bark")


class Cat(Animal):
    pass


dog1 = Dog()
dog1.bark() #Can get 2 methods to call, since 1 is inherited
cat1 = Cat()
cat1.walk()

#o/p
#bark
#walk