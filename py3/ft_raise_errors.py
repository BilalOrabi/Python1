def check_plant_health(
    plant_name: str, water_level: int, sunlight_hours: int
) -> str:
    """Check the health of a plant based on its name, water level,
    and sunlight hours."""

    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level < 1:
        raise ValueError(f"Water level {water_level} is low! (min 1)")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is high (max 10)")

    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is low (min 2)")

    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is high (max 12)")

    return f"Plant '{plant_name}' is healthy!"


def test_plant_checks() -> None:
    """Test the plant health checks for various scenarios."""
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        result = check_plant_health("tomato", 5, 6)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print()

    print("Testing empty plant name...")
    try:
        result = check_plant_health("", 5, 6)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print()

    print("Testing bad water level...")
    try:
        result = check_plant_health("tomato", 15, 6)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print()

    print("Testing bad sunlight hours...")
    try:
        result = check_plant_health("tomato", 5, 0)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
