class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.growth = 0

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")

    def grow(self, additional_growth: float) -> None:
        if additional_growth < 0:
            raise ValueError("Growth cannot be negative.")
        self.height += additional_growth
        self.growth += additional_growth

    def add_age(self, days: int) -> None:
        if days < 0:
            raise ValueError("Age increment cannot be negative.")
        self.age += days

    def get_status(self) -> None:
        self.display_info()
        if self.growth > 0:
            print(f"Growth this week: +{self.growth}cm")


if __name__ == "__main__":

    plant1 = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    plant1.get_status()
    plant1.grow(6)
    plant1.add_age(6)
    print("=== Day 7 ===")
    plant1.get_status()
