class DogClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof! woof! and i am {self.age} years old")


obj_1 = DogClass("Lex", 5)
obj_2 = DogClass("Max", 7)

print(obj_1.bark())
print(obj_2.bark())