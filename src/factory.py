from abc import ABC, abstractmethod
from random import choice


class BasePlayer(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(BasePlayer):

    def move(self):
        mov = input('choose your next move: ')
        return mov


class SystemPlayer(BasePlayer):

    def move(self):
        mov = choice(self.choices)
        print( f'System choice is {mov}')


class Game:
    @staticmethod
    def start_game():
        game_type = input("Please chose game type(s -> single player , m -> multiple player): ")
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()

        elif game_type == 'm':
            p1 = HumanPlayer()
            p2 = HumanPlayer()

        else:
            print("Invalid input")
            Game.start_game()
        return p1, p2

if __name__ == "__main__":
    player1, player2 = Game().start_game()

    for player in [player1, player2]:
        p = player.move()

















