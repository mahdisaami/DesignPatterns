import random
from abc import ABC, abstractmethod


class Lift:
    floors = list(range(41))

    def __init__(self):
        self.floor = 1
        self.flow = []

    @property
    def current_user(self):
        return self.flow[-1]

    def up_down(self, user, floor):
        if self.floor != floor:
            if floor not in user.allowed_floors:
                print(f'Sorry! {user.name} are not allowed to go floor {floor}')
            else:
                self.flow.append(user)
                self.floor = floor
                print(f'Hi dear {user.name}, you are heading to floor {floor}  ')
        else:
            print(f'Dear {user.name}, you are already in floor {floor}')


class AbstractUser(ABC):
    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def allowed_floors(self):
        pass

class Manager(AbstractUser):
    allowed_floors = list(range(41))

class Supervisor(AbstractUser):
    allowed_floors = list(range(31))

class Staff(AbstractUser):
    allowed_floors = list(range(21))

class Client(AbstractUser):
    allowed_floors = list(range(11))

if __name__ == '__main__':


    manager = Manager('Mahdi')
    supervisor = Supervisor('Ali')
    staff = Staff('Sara')
    client = Client('Ehsan')

    lift = Lift()

    lift.up_down(manager, 40)
    lift.up_down(supervisor, 39)
    lift.up_down(staff, 10)
    lift.up_down(client, 42)




