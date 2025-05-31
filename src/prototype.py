import copy

class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def clone(self, color):
        new = copy.deepcopy(self)
        new.color = color
        return new

if __name__ == '__main__':

    car1 = Car("Toyota", "Red")
    car2 = car1.clone("Blue")

    print(car1.brand, car1.color)
    print(car2.brand, car2.color)


       #### WHEN TO USE IT ####
# When object creation is expensive or complex.
# When you want to avoid subclassing for every object type.
# When you need to create many similar objects.