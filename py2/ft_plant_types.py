class Plant:
    def __init__(self, name, height=None, age=None):
        self._name = name
        self._height = 0
        self._age = 0
        if height is not None:
            self.set_height(height)
        if age is not None:
            self.set_age(age)

    def _security_error(self, field, value, unit):
        print(
            f"Invalid operation attempted: {field} {value}{unit} [REJECTED]"
        )
        print(f"Security: Negative {field} rejected")

    def set_height(self, height):
        if height < 0:
            self._security_error("height", height, "cm")
            return
        self._height = height

    def set_age(self, age):
        if age < 0:
            self._security_error("age", age, " days")
            return
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def describe(self):
        print(
            f"{self._name} (Flower): "
            f"{self._height}cm, {self._age} days, {self.color} color"
        )

    def bloom(self):
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def describe(self):
        print(
            f"{self._name} (Tree): "
            f"{self._height}cm, {self._age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self):
        shade = self.trunk_diameter * 1.56
        print(
            f"{self._name} provides "
            f"{int(shade)} square meters of shade"
        )


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self):
        print(
            f"{self._name} (Vegetable): "
            f"{self._height}cm, {self._age} days, "
            f"{self.harvest_season.lower()} harvest"
        )

    def nutrition_info(self):
        print(
            f"{self._name} is rich in {self.nutritional_value}"
        )


def main():
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    rose.describe()
    rose.bloom()

    print()

    oak = Tree("Oak", 500, 1825, 50)
    oak.describe()
    oak.produce_shade()

    print()

    tomato = Vegetable("Tomato", 80, 90, "Summer", "vitamin C")
    tomato.describe()
    tomato.nutrition_info()


if __name__ == "__main__":
    main()
