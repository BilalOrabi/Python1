import sys


def main() -> None:
    args = sys.argv
    total_args = len(args)

    print("=== Command Quest ===")
    print(f"Program name: {args[0]}")

    if total_args == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {total_args - 1}")

        for i in range(1, total_args):
            print(f"Argument {i}: {args[i]}")

    print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
