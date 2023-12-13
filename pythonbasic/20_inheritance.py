# Inheritance means - taking properties from our parents
#e.g. inheriting qualities from parents

class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog1 = Dog()
dog1.walk()
cat1 = Cat()
cat1.walk()

#o/p
#walk
#walk

