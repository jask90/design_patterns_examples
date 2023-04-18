import copy


class StormTropper:
    def __init__(
            self, armor_color, blaster_type, additional_equipments, army
    ) -> None:
        self.armor_color = armor_color
        self.blaster_type = blaster_type
        self.additional_equipments = additional_equipments
        self.army = army

    def shoot(self):
        print(f'Firing {self.blaster_type} blaster rifle')
    
    def show_equipments(self):
        print(f'{self.additional_equipments}')
    
    def show_army(self):
        print(f'{self.army}')


class StormTropperPrototype:
    def __init__(self) -> None:
        self.storm_tropper = None

    def clone(self):
        return copy.copy(self.storm_tropper)
    
    def deep_clone(self, memo=None):
        if memo is None:
            memo = {}
        return copy.deepcopy(self.storm_tropper, memo)


if __name__ == "__main__":
    # Compare cloning behavior
    # With Copy
    storm_tropper_army = []
    storm_tropper_prototype = StormTropperPrototype()
    storm_tropper_prototype.storm_tropper = StormTropper(
        armor_color="black", blaster_type="basic", additional_equipments=[
            "grenades", "knives"
        ],
        army=storm_tropper_army
    )

    for i in range(5):
        new_storm_tropper = storm_tropper_prototype.clone()
        new_storm_tropper.shoot()
        storm_tropper_army.append(new_storm_tropper)

    # Change equipment
    storm_tropper_army[0].blaster_type = "advanced"
    storm_tropper_army[0].additional_equipments.append("energy shield")

    for storm_tropper in storm_tropper_army:
        storm_tropper.shoot()
        storm_tropper.show_equipments()
        storm_tropper.show_army()

    # With Deep Copy
    storm_tropper_army.clear()
    storm_tropper_prototype.storm_tropper = StormTropper(
        armor_color="black", blaster_type="basic", additional_equipments=[
            "grenades", "knives"
        ],
        army=storm_tropper_army
    )

    for i in range(5):
        new_storm_tropper = storm_tropper_prototype.deep_clone()
        new_storm_tropper.shoot()
        storm_tropper_army.append(new_storm_tropper)

    # Change equipment
    storm_tropper_army[0].blaster_type = "advanced"
    storm_tropper_army[0].additional_equipments.append("energy shield")

    for storm_tropper in storm_tropper_army:
        storm_tropper.shoot()
        storm_tropper.show_equipments()
        storm_tropper.show_army()
