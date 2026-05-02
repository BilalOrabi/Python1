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
            print(f"File '{filename}' closed.")


def transform_content(content: str) -> str:
    lines = content.splitlines()
    result = []

    for line in lines:
        result.append(line + "#")

    return "\n".join(result)


def save_file(filename: str, content: str) -> None:
    file = None
    try:
        file = open(filename, "w")
        file.write(content + "\n")
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

        print("---")
        print(content, end="" if content.endswith("\n") else "\n")
        print("---")

        print("Transform data:")
        print("---")

        transformed = transform_content(content)
        print(transformed)
        print("---")

        new_filename = input("Enter new file name (or empty): ")

        if new_filename:
            save_file(new_filename, transformed)
            print(f"Data successfully saved to '{new_filename}'")
        else:
            print("Not saving data.")

    except OSError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    main()
