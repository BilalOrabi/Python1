import alchemy.transmutation as transmutation


def main() -> None:
    print("=== Transmutation 1 ===")
    print("Import transmutation module directly")

    print(
        "Testing lead to gold: "
        f"{transmutation.recipes.lead_to_gold()}"
    )

if __name__ == "__main__":
    main()