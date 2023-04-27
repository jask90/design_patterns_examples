
class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            instance = super().__new__(cls, *args, **kwargs)
            cls._instance = instance
        return cls._instance


class Game(Singleton):
    pass


if __name__ == "__main__":
    # The client code.

    g1 = Game()
    g2 = Game()

    if id(g1) == id(g2):
        print("Singleton works, both variables contain the same instance.")
    else:
        print("Singleton failed, variables contain different instances.")
