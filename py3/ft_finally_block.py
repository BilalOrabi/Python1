
def water_plants(plant_list: list[str]) -> None:
    """Simulate watering plants with error handling and cleanup."""
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None- invalid plant!")
            print(f"Watering {plant}")
        print("Watering completed successfully!")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """Test the watering system with both valid and invalid plant lists."""
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print()

    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("\n")
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
