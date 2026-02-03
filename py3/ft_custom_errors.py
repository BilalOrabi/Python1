# ft_custom_errors.py

class GardenError(Exception):
    """Base class for all garden-related errors."""
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class PlantError(GardenError):
    """Raised for errors related to plants."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    """Raised for errors related to watering."""
    def __init__(self, message: str) -> None:
        super().__init__(message)


def plant_growth_check(plant_type: str) -> str:
    """Simulate checking plant growth, raising an error for wilting plants."""
    if plant_type == "wilting":
        raise PlantError("The tomato plant is wilting!")
    return f"The {plant_type} plant is healthy."


def water_plant(water_level: int) -> str:
    """Simulate watering a plant, raising an error for insufficient water."""
    if water_level <= 0:
        raise WaterError("Not enough water in the tank!")
    elif water_level > 100:
        raise WaterError("Too much water! The plant is drowning.")
    return "The plant has been watered successfully."


def garden_simulation() -> None:
    """Main function to demonstrate custom garden error handling."""
    print("=== Custom Garden Errors Demo ===")
    print("\nTesting PlantError...")
    try:
        print(plant_growth_check("wilting"))
    except PlantError as e:
        print(f"Caught PlantError: {e}")

    print("\nTesting WaterError...")
    try:
        print(water_plant(0))
    except WaterError as e:
        print(f"Caught WaterError: {e}")

    print("\nTesting catching all garden errors...")
    try:
        print(plant_growth_check("wilting"))
        print(water_plant(0))
    except GardenError as e:
        print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    garden_simulation()
