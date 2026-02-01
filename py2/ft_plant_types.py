class Plant:
    _name: str
    _height: float
    _age: int

    def __init__(
        self,
        name: str,
        height: float | None = None,
        age: int | None = None,
    ) -> None:
        self._name = name
        self._height = 0
        self._age = 0
        if height is not None:
            self.set_height(height)
        if age is not None:
            self.set_age(age)

    def _security_error(
        self, field: str, value: float | int, unit: str
    ) -> None:
        print(
            f"Invalid operation attempted: {field} {value}{unit} [REJECTED]"
        )
        print(f"Security: Negative {field} rejected")

    def set_height(self, height: float) -> None:
        if height < 0:
            self._security_error("height", height, "cm")
            return
        self._height = height

    def set_age(self, age: int) -> None:
        if age < 0:
            self._security_error("age", age, " days")
            return
        self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name


class Flower(Plant):
    color: str

    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color

    def describe(self) -> None:
        print(
            f"{self._name} (Flower): "
            f"{self._height}cm, {self._age} days, {self.color} color"
        )

    def bloom(self) -> None:
        print(f"{self._name} is blooming beautifully!")


class Tree(Plant):
    trunk_diameter: float

    def __init__(
        self, name: str, height: float, age: int, trunk_diameter: float
    ) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def describe(self) -> None:
        print(
            f"{self._name} (Tree): "
            f"{self._height}cm, {self._age} days, "
            f"{self.trunk_diameter}cm diameter"
        )

    def produce_shade(self) -> None:
        shade = self.trunk_diameter * 1.56
        print(
            f"{self._name} provides "
            f"{int(shade)} square meters of shade"
        )


class Vegetable(Plant):
    harvest_season: str
    nutritional_value: str

    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        harvest_season: str,
        nutritional_value: str,
    ) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def describe(self) -> None:
        print(
            f"{self._name} (Vegetable): "
            f"{self._height}cm, {self._age} days, "
            f"{self.harvest_season.lower()} harvest"
        )

    def nutrition_info(self) -> None:
        print(
            f"{self._name} is rich in {self.nutritional_value}"
        )


def main() -> None:
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
