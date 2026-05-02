import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")

        if len(parts) != 3:
            print("Invalid syntax")
            continue

        values = []
        error_occurred = False

        for part in parts:
            part = part.strip()
            try:
                values.append(float(part))
            except ValueError:
                print(
                    f"Error on parameter '{part}': "
                    f"could not convert string to float: '{part}'"
                )
                error_occurred = True
                break

        if error_occurred:
            continue

        return (values[0], values[1], values[2])


def distance(
    pos1: tuple[float, float, float],
    pos2: tuple[float, float, float],
) -> float:
    return math.sqrt(
        (pos2[0] - pos1[0]) ** 2 +
        (pos2[1] - pos1[1]) ** 2 +
        (pos2[2] - pos1[2]) ** 2
    )


def main() -> None:
    print("=== Game Coordinate System ===\n")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    center = (0.0, 0.0, 0.0)
    dist_center = distance(pos1, center)
    print(f"Distance to center: {round(dist_center, 4)}\n")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_between = distance(pos1, pos2)
    print(
        "Distance between the 2 sets of coordinates: "
        f"{round(dist_between, 4)}"
    )


if __name__ == "__main__":
    main()
