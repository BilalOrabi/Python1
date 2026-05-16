import alchemy.elements


def main() -> None:
    print("=== Alembic 2 ===")
    print("Using: 'import ...' structure to access alchemy.elements.py")
    print(f"Testing create_earth: {alchemy.elements.create_earth()}")

if __name__ == "__main__":
    main()