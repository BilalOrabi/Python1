class Plant:
    def __init__(self, name):
        self._name = name
        self._height = 0
        self._age = 0
        print(f"Plant created: {self._name}")

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
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            self._security_error("age", age, " days")
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_name(self):
        return self._name

def main():
    print("=== Garden Security System ===")

    plant = Plant("Rose")
    plant.set_height(25)
    plant.set_age(30)

    print()
    plant.set_height(-5)

    print()
    print(
        f"Current plant: {plant.get_name()} "
        f"({plant.get_height()}cm, {plant.get_age()} days)"
    )

if __name__ == "__main__":
    
    main()