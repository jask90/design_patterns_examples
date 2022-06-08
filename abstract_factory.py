
class Wall:

    def random_method(self) -> str:
        return 'This is a Wall'


class Door:

    def random_method(self) -> str:
        return 'This is a Door'


class Roof:

    def random_method(self) -> str:
        return 'This is a Roof'


class ModernWall(Wall):

    def random_method(self) -> str:
        return 'This is a Modern Wall'


class ModernDoor(Door):

    def random_method(self) -> str:
        return 'This is a Modern Door'


class ModernRoof(Roof):

    def random_method(self) -> str:
        return 'This is a Modern Roof'


class JapaneseWall(Wall):

    def random_method(self) -> str:
        return 'This is a Japanese Wall'


class JapaneseDoor(Door):

    def random_method(self) -> str:
        return 'This is a Japanese Door'


class JapaneseRoof(Roof):

    def random_method(self) -> str:
        return 'This is a Japanese Roof'


class HouseFactory:

    def create_wall(self) -> Wall:
        return Wall()

    def create_door(self) -> Door:
        return Door()

    def create_roof(self) -> Roof:
        return Roof()


class ModernHouseFactory(HouseFactory):

    def create_wall(self) -> ModernWall:
        return ModernWall()

    def create_door(self) -> ModernDoor:
        return ModernDoor()

    def create_roof(self) -> ModernRoof:
        return ModernRoof()


class JapaneseHouseFactory(HouseFactory):

    def create_wall(self) -> JapaneseWall:
        return JapaneseWall()

    def create_door(self) -> JapaneseDoor:
        return JapaneseDoor()

    def create_roof(self) -> JapaneseRoof:
        return JapaneseRoof()


def client(factory: HouseFactory):
    """Function were we will create the elements of the house.
    This function only use methods defined in the Abstract classes.

    Args:
        factory (HouseFactory): Factory used to create all the elements of the house.
    """    
    wall = factory.create_wall()
    door = factory.create_door()
    roof = factory.create_roof()

    print(wall.random_method())
    print(door.random_method())
    print(roof.random_method())


if __name__ == '__main__':
    # House
    print('House')
    factory = HouseFactory()
    client(factory)

    # Japanese House
    print('Japanese House')
    factory = JapaneseHouseFactory()
    client(factory)

    # Modern House
    print('Moderns House')
    factory = ModernHouseFactory()
    client(factory)
