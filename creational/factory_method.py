from abc import ABC, abstractmethod


class Character(ABC):

    @abstractmethod
    def talk(self):
        pass


class Game(ABC):
    """
    Game implements the create_character method to return a character class.
    The Game subclasses will implement the call to the
    Character subclass required for each case.
    """

    @abstractmethod
    def create_character(self) -> Character:
        pass

    def use_character(self):
        character = self.create_character()
        character.talk()


class WizardsGame(Game):

    def create_character(self) -> Character:
        return Wizard()


class Wizard(Character):

    def talk(self):
        print('I am a Magician')


class StarWarsGame(Game):

    def create_character(self) -> Character:
        return Stormtrooper()


class Stormtrooper(Character):

    def talk(self):
        print('I am a Stormtrooper')


def client_code(game: Game):
    """
    The client will receive a Game subclass 
    that will create the type of Character required for each case
    """
    game.use_character()


if __name__ == "__main__":
    print("Initializing WizardsGame")
    client_code(WizardsGame())

    print("Initializing StarWarsGame")
    client_code(StarWarsGame())
