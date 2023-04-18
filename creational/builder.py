from dataclasses import dataclass, field

# Construir casas

# Constructor   ->  Constructor de casas abstract
# Constructor Concreto
# Director
# Producto


@dataclass
class Wall:
    description: str


@dataclass
class Door:
    description: str


@dataclass
class Roof:
    description: str


@dataclass
class House:
    walls: list[Wall] = field(default_factory=list)
    doors: list[Door] = field(default_factory=list)
    roofs: list[Roof] = field(default_factory=list)

    def add_wall(self, wall: Wall) -> None:
        self.walls.append(wall)

    def add_door(self, door: Door) -> None:
        self.doors.append(door)

    def add_roof(self, roof: Roof) -> None:
        self.roofs.append(roof)


class HouseBuilder:

    @property
    def house() -> None:
        pass

    def build_wall(self) -> None:
        pass

    def build_door(self) -> None:
        pass

    def build_roof(self) -> None:
        pass


@dataclass
class JapaneseHouseBuilder(HouseBuilder):
    _house: House = field(init=False)

    def __post_init__(self) -> None:
        self.reset()
    
    def reset(self):
        self._house = House()

    @property
    def house(self) -> House:
        return self._house

    def build_wall(self) -> None:
        wall = Wall(description='Japanese Wall')
        self._house.add_wall(wall)

    def build_door(self) -> None:
        door = Door(description='Japanese Door')
        self._house.add_door(door)

    def build_roof(self) -> None:
        roof = Roof(description='Japanese Roof')
        self._house.add_roof(roof)


@dataclass
class Director:
    builder: HouseBuilder

    def build_small_house(self) -> None:
        self.builder.build_roof()

        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()

        self.builder.build_door()


    def build_big_house(self) -> None:
        self.builder.build_roof()
        self.builder.build_roof()

        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()
        self.builder.build_wall()

        self.builder.build_door()
        self.builder.build_door()


def client():
    builder = JapaneseHouseBuilder()
    director = Director(builder=builder)

    director.build_small_house()
    print('**** Small House ****')
    print(director.builder.house)

    director.builder.reset()

    director.build_big_house()
    print('**** Big House ****')
    print(director.builder.house)


if __name__ == '__main__':
    client()
