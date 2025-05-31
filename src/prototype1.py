import copy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

    def clone(self, age):
        new_person = copy.deepcopy(self)
        new_person.__dict__.update(age)
        return new_person



if __name__ == "__main__":

    p1 = Person("Ali", 30)
    print("Original:", p1)

    p2 = p1.clone(25)
    print("Cloned:", p2)