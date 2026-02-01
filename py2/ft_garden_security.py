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
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age: int) -> None:
        if age < 0:
            self._security_error("age", age, " days")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_name(self) -> str:
        return self._name


def main() -> None:
    print("=== Garden Security System ===")

    plant = Plant("Rose", 25, 30)
    print(f"Plant created: {plant.get_name()}")

    print()
    plant.set_height(-5)

    print()
    print(
        f"Current plant: {plant.get_name()} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )


if __name__ == "__main__":
    main()
