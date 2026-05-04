import sys


def read_file(filename: str) -> str:
    file = None
    try:
        file = open(filename, "r")
        content = file.read()
        return content
    finally:
        if file:
            file.close()


def transform_content(content: str) -> str:
    lines = content.splitlines()
    result = []

    for line in lines:
        result.append(line + "#")

    return "\n".join(result)


def save_file(filename: str, content: str) -> bool:
    file = None
    try:
        file = open(filename, "w")
        file.write(content + "\n")
        return True
    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)
        return False
    finally:
        if file:
            file.close()


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    filename = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        content = read_file(filename)

        print("---\n")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

        print(f"\nFile '{filename}' closed.\n")

        print("Transform data:")
        print("---\n")

        transformed = transform_content(content)
        print(transformed)
        print("\n---")

        print("Enter new file name (or empty): ", end="", flush=True)
        new_filename = sys.stdin.readline().rstrip("\n")

        if new_filename:
            print(f"Saving data to '{new_filename}'")
            if save_file(new_filename, transformed):
                print(f"Data successfully saved to '{new_filename}'")
            else:
                print("Data not saved.")
        else:
            print("Not saving data.")

    except OSError as e:
        print(
            f"[STDERR] Error opening file '{filename}': {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
