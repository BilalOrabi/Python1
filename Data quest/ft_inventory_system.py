import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = {}

    for arg in args:
        if ":" not in arg:
            print(f"Error - invalid parameter '{arg}'")
            continue

        name, quantity_str = arg.split(":", 1)

        if name in inventory:
            print(f"Redundant item '{name}' - discarding")
            continue

        try:
            quantity = int(quantity_str)
        except ValueError:
            print(
                f"Quantity error for '{name}': "
                f"invalid literal for int() with base 10: "
                f"'{quantity_str}'"
            )
            continue

        inventory[name] = quantity

    return inventory


def main() -> None:
    print("=== Inventory System Analysis ===")

    args: list[str] = sys.argv[1:]
    inventory = parse_inventory(args)

    print(f"Got inventory: {inventory}")

    if not inventory:
        return

    items = list(inventory.keys())
    print(f"Item list: {items}")

    total_quantity = sum(inventory.values())
    print(
        f"Total quantity of the {len(items)} items: "
        f"{total_quantity}"
    )

    for item, qty in inventory.items():
        percentage = (qty / total_quantity) * 100
        print(f"Item {item} represents {percentage:.1f}%")

    most_item: str = ""
    least_item: str = ""

    for item, qty in inventory.items():
        if most_item == "" or qty > inventory[most_item]:
            most_item = item
        if least_item == "" or qty < inventory[least_item]:
            least_item = item

    print(
        f"Item most abundant: {most_item} "
        f"with quantity {inventory[most_item]}"
    )
    print(
        f"Item least abundant: {least_item} "
        f"with quantity {inventory[least_item]}"
    )

    new_data = {"magic_item": 1}
    inventory.update(new_data)
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
