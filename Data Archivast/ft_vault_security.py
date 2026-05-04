

def secure_archive(
    filename: str, mode: str = "r", content: str = ""
) -> tuple[bool, str]:
    try:
        if mode == "r":
            with open(filename, "r") as file_var:
                data = file_var.read()
                return (True, data)

        elif mode == "w":
            with open(filename, "w") as file_var:
                file_var.write(content)
                return (True, "Content successfully written to file")

        else:
            return (False, "Invalid mode")

    except OSError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("\nUsing ’secure_archive’ to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "r"))

    print("\nUsing ’secure_archive’ to read from an inaccessible file:")
    print(secure_archive(r"C:\PerfLogs", "r"))

    print("\nUsing ’secure_archive’ to read from a regular file:")
    success, data = secure_archive("ancient_fragment.txt", "r")
    print((success, data))

    print("\nUsing ’secure_archive’ to write previous content to a new file:")
    if success:
        print(secure_archive("new_archive.txt", "w", data))
    else:
        print((False, "No data to write"))


if __name__ == "__main__":
    main()
