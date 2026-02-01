def check_temperature(temp_str: str) -> str:
    """
    Check if a temperature value is within acceptable range for plants.

    Converts the input string to an integer and validates it's between
    0°C and 40°C. Returns appropriate error or success message.

    Args:
        temp_str: String representation of temperature value.

    Returns:
        String message indicating if temperature is valid for plants.
    """
    try:
        temp: int = int(temp_str)

        if temp < 0:
            return f"Error: {temp}°C is too cold for plants (min 0°C)"
        elif temp > 40:
            return f"Error: {temp}°C is too hot for plants (max 40°C)"
        else:
            return f"Temperature {temp}°C is perfect for plants!"
    except ValueError:
        return f"Error: '{temp_str}' is not a valid number"


def test_temperature_input() -> None:
    """
    Test the temperature checker with various valid and invalid inputs.

    Runs multiple test cases including valid temperatures, non-numeric input,
    and extreme temperature values to verify exception handling.
    """
    print("=== Garden Temperature Checker ===\n")

    print("Testing temperature:", "25")
    print(check_temperature("25"))

    print("\nTesting temperature:", "abc")
    print(check_temperature("abc"))

    print("\nTesting temperature:", "100")
    print(check_temperature("100"))

    print("\nTesting temperature:", "-50")
    print(check_temperature("-50"))

    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
