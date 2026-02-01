class Plant:
    """Base class for all plants in the garden."""

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
        self._height = 0.0
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

    def grow(self, growth: float) -> None:
        """Grow the plant by a specified amount in cm."""
        if growth > 0:
            self.set_height(self._height + growth)


class FloweringPlant(Plant):
    """Plant that produces flowers."""

    _flowers: int
    _flower_color: str

    def __init__(
        self,
        name: str,
        height: float | None = None,
        age: int | None = None,
        flower_color: str = "white",
    ) -> None:
        super().__init__(name, height, age)
        self._flowers = 0
        self._flower_color = flower_color

    def bloom(self, flower_count: int) -> None:
        """Add flowers to the plant."""
        if flower_count < 0:
            print("Security: Negative flower count rejected")
            return
        self._flowers = flower_count
        msg = (f"{self._name} is blooming with {flower_count} "
               f"{self._flower_color} flowers (blooming)")
        print(msg)

    def get_flowers(self) -> int:
        return self._flowers

    def get_flower_color(self) -> str:
        return self._flower_color


class PrizeFlower(FloweringPlant):
    """Special flowering plant that can win prizes."""

    _prize_points: int

    def __init__(
        self,
        name: str,
        height: float | None = None,
        age: int | None = None,
        flower_color: str = "white",
    ) -> None:
        super().__init__(name, height, age, flower_color)
        self._prize_points = 0

    def award_points(self, points: int) -> None:
        """Award prize points to this plant."""
        if points < 0:
            print("Security: Negative prize points rejected")
            return
        self._prize_points = points

    def get_prize_points(self) -> int:
        return self._prize_points


class Garden:
    """Manages a collection of plants and their statistics."""

    _name: str
    _plants: list[Plant]

    def __init__(self, name: str) -> None:
        self._name = name
        self._plants = []

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self._plants.append(plant)
        print(f"Added {plant.get_name()} to {self._name}'s garden")

    def get_plants(self) -> list[Plant]:
        """Return all plants in the garden."""
        return self._plants

    def get_name(self) -> str:
        return self._name

    def help_grow(self, growth: float) -> None:
        """Help all plants grow by a specified amount."""
        print(f"{self._name} is helping all plants grow...")
        for plant in self._plants:
            plant.grow(growth)

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        @staticmethod
        def total_plants(garden: "Garden") -> int:
            """Calculate total number of plants."""
            return len(garden.get_plants())

        @staticmethod
        def total_growth(garden: "Garden") -> float:
            """Calculate total growth across all plants."""
            return sum(plant.get_height() for plant in garden.get_plants())

        @staticmethod
        def average_height(garden: "Garden") -> float:
            """Calculate average height of plants."""
            plants = garden.get_plants()
            if not plants:
                return 0.0
            return Garden.GardenStats.total_growth(garden) / len(plants)

        @staticmethod
        def plant_types(garden: "Garden") -> dict[str, int]:
            """Count different types of plants."""
            types: dict[str, int] = {
                "regular": 0,
                "flowering": 0,
                "prize flowers": 0,
            }
            for plant in garden.get_plants():
                if isinstance(plant, PrizeFlower):
                    types["prize flowers"] += 1
                elif isinstance(plant, FloweringPlant):
                    types["flowering"] += 1
                else:
                    types["regular"] += 1
            return types


class GardenManager:
    """Manages multiple gardens and provides analytics."""

    _gardens: dict[str, Garden]

    def __init__(self) -> None:
        self._gardens = {}

    def create_garden(self, gardener_name: str) -> Garden:
        """Create a new garden for a gardener."""
        garden = Garden(gardener_name)
        self._gardens[gardener_name] = garden
        return garden

    def get_garden(self, gardener_name: str) -> Garden | None:
        """Retrieve a garden by gardener name."""
        return self._gardens.get(gardener_name)

    def get_gardens(self) -> dict[str, Garden]:
        """Get all gardens managed."""
        return self._gardens

    @classmethod
    def create_garden_network(cls) -> "GardenManager":
        """Class method to create a new garden manager instance."""
        return cls()

    def generate_report(self, gardener_name: str) -> None:
        """Generate a detailed report for a specific garden."""
        garden = self.get_garden(gardener_name)
        if not garden:
            print(f"Garden for {gardener_name} not found")
            return

        stats = Garden.GardenStats
        print(f"\n=== {gardener_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in garden.get_plants():
            if isinstance(plant, PrizeFlower):
                msg = (f"- {plant.get_name()}: {plant.get_height()}cm, "
                       f"{plant.get_flowers()} {plant.get_flower_color()} "
                       f"flowers (blooming), Prize points: "
                       f"{plant.get_prize_points()}")
                print(msg)
            elif isinstance(plant, FloweringPlant):
                msg = (f"- {plant.get_name()}: {plant.get_height()}cm, "
                       f"{plant.get_flowers()} {plant.get_flower_color()} "
                       f"flowers (blooming)")
                print(msg)
            else:
                print(f"- {plant.get_name()}: {plant.get_height()}cm")
        print(f"\nPlants added: {stats.total_plants(garden)}, "
              f"Total growth: {stats.total_growth(garden)}cm")
        plant_count = stats.plant_types(garden)
        msg = (f"Plant types: {plant_count['regular']} regular, "
               f"{plant_count['flowering']} flowering, "
               f"{plant_count['prize flowers']} prize flowers")
        print(msg)

    def total_gardens_managed(self) -> int:
        """Instance method: return number of gardens managed."""
        return len(self._gardens)

    def validate_all_heights(self) -> bool:
        """Validate that all plants have valid heights."""
        for garden in self._gardens.values():
            for plant in garden.get_plants():
                if plant.get_height() < 0:
                    return False
        return True


def print_statistics(manager: GardenManager) -> None:
    """Print statistics across all gardens."""
    total = manager.total_gardens_managed()
    print(f"Total gardens managed: {total}")


def calculate_network_growth(manager: GardenManager) -> float:
    """Calculate total growth across all gardens."""
    total = 0.0
    for garden in manager.get_gardens().values():
        total += Garden.GardenStats.total_growth(garden)
    return total


def main() -> None:
    """Main demonstration of the Garden Management System."""
    print("=== Garden Management System Demo ===\n")

    # Create a garden manager
    manager: GardenManager = GardenManager.create_garden_network()

    # Create gardens for Alice and Bob
    alice_garden: Garden = manager.create_garden("Alice")
    bob_garden: Garden = manager.create_garden("Bob")

    # Alice's garden setup
    oak_tree: Plant = Plant("Oak Tree", height=100.0)
    alice_garden.add_plant(oak_tree)

    rose: FloweringPlant = FloweringPlant(
        "Rose", height=25.0, flower_color="red"
    )
    alice_garden.add_plant(rose)
    rose.bloom(1)

    sunflower: PrizeFlower = PrizeFlower(
        "Sunflower", height=50.0, flower_color="yellow"
    )
    alice_garden.add_plant(sunflower)
    sunflower.bloom(1)
    sunflower.award_points(10)

    # Bob's garden setup
    daisy: FloweringPlant = FloweringPlant(
        "Daisy", height=20.0, flower_color="white"
    )
    bob_garden.add_plant(daisy)
    daisy.bloom(5)

    lily: PrizeFlower = PrizeFlower(
        "Lily", height=30.0, flower_color="pink"
    )
    bob_garden.add_plant(lily)
    lily.bloom(3)
    lily.award_points(7)

    tulip: Plant = Plant("Tulip", height=15.0)
    bob_garden.add_plant(tulip)

    # Help plants grow
    print("\nAlice is helping all plants grow...")
    alice_garden.help_grow(1.0)

    # Generate reports
    manager.generate_report("Alice")
    manager.generate_report("Bob")

    # Validate heights
    is_valid = manager.validate_all_heights()
    print(f"\nHeight validation test: {is_valid}")

    # Calculate and display garden scores
    alice_height: float = Garden.GardenStats.total_growth(
        alice_garden
    )
    bob_height: float = Garden.GardenStats.total_growth(bob_garden)
    alice_score: int = int(alice_height) + sum(
        plant.get_prize_points() if isinstance(plant, PrizeFlower)
        else 0
        for plant in alice_garden.get_plants()
    )
    bob_score: int = int(bob_height) + sum(
        plant.get_prize_points() if isinstance(plant, PrizeFlower)
        else 0
        for plant in bob_garden.get_plants()
    )

    msg = f"Garden scores - Alice: {alice_score}, Bob: {bob_score}"
    print(msg)

    # Print overall statistics
    print_statistics(manager)


if __name__ == "__main__":
    main()
