class GardenError(Exception):
    """Base class for all garden-related errors."""
    pass


class PlantError(GardenError):
    """Raised for errors related to plants."""
    pass


class WaterError(GardenError):
    """Raised for errors related to watering."""
    pass


class Plant:
    """Class representing a plant in the garden."""
    def __init__(self, plant_name: str, water_level: int,
                 sunlight_hours: int) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")
        if water_level < 0:
            raise WaterError("Water level cannot be negative!")
        if sunlight_hours < 0:
            raise GardenError("Sunlight hours cannot be negative!")

        self.plant_name = plant_name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:
    """Class to manage garden plants and watering system."""
    def __init__(self) -> None:
        self.plants_list = []

    def add_plant(self, plant: Plant) -> None:
        """Adds a plant to the garden."""
        self.plants_list.append(plant)
        print(f"Added {plant.plant_name} successfully")

    def water_plants(self) -> None:
        """Simulate watering plants with resource management."""
        print("\nWatering plants...")
        try:
            print("Opening watering system")
            if not self.plants_list:
                raise WaterError("No plants to water!")

            for plant in self.plants_list:
                print(f"Watering {plant.plant_name}- success")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self) -> None:
        """Check the health of all plants in the garden."""
        print("\nChecking plant health...")
        for plant in self.plants_list:
            try:
                if plant.water_level > 10:
                    raise WaterError(
                        f"Water level {plant.water_level} is too high "
                        f"(max 10)")
                if plant.sunlight_hours < 2:
                    raise GardenError(
                        f"Sunlight level {plant.sunlight_hours} is too low "
                        f"(min 2)")

                print(
                    f"{plant.plant_name}: healthy "
                    f"(water: {plant.water_level}, sun: "
                    f"{plant.sunlight_hours})")
            except (GardenError, WaterError) as e:
                print(f"Error checking {plant.plant_name}: {e}")


def main() -> None:
    """Main function to test the garden management system."""
    print("=== Garden Management System ===")

    garden = GardenManager()

    print("\nAdding plants to garden...")
    try:
        garden.add_plant(Plant("tomato", 5, 8))
    except PlantError as pe:
        print(f"Error adding plant: {pe}")

    try:
        garden.add_plant(Plant("lettuce", 15, 5))
    except PlantError as pe:
        print(f"Error adding plant: {pe}")

    try:
        garden.add_plant(Plant("", 3, 8))
    except PlantError as pe:
        print(f"Error adding plant: {pe}")

    garden.water_plants()

    garden.check_plant_health()

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as ge:
        print(f"Caught GardenError: {ge}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
