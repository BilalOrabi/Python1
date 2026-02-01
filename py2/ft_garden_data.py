class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def display_info(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")
        return None


if __name__ == "__main__":
    Plant1 = Plant("Rose", 25, 30)
    Plant2 = Plant("Sunflower", 80, 45)
    Plant3 = Plant("Cactus", 15, 120)
    print("=== Garden Plant Registry ===")
    Plant1.display_info()
    Plant2.display_info()
    Plant3.display_info()
