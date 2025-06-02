import random


class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def create(name):
        if name:
            return User(name)
        return ValueError("It is not valid")


class Game:
    def __init__(self, u1, u2):
        self.u1 = u1
        self.u2 = u2
        self.turn = u1

    def change_turn(self):
        self.turn = self.u2 if self.turn == self.u1 else self.u1

    def roll_dice(self, user):
        if self.turn == user:
            self.change_turn()
            return f"{user.name}: {random.randint(1, 6)}"
        return ValueError(f"Not your turn {user.name}")

if __name__ == "__main__":

    us1 = User.create("Mahdi")
    us2 = User.create("Sara")

    print(us1)
    print(us2)


    game = Game(us1, us2)

    print(game.roll_dice(us1))
    print(game.roll_dice(us1))
    print(game.roll_dice(us2))
    print(game.roll_dice(us2))
    print(game.roll_dice(us2))
    print(game.roll_dice(us1))
    print(game.roll_dice(us1))
    print(game.roll_dice(us2))
