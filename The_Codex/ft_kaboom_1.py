print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py dirctly")
print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")

from alchemy.grimoire.dark_spellbook import dark_spell_record

def main() -> None:
    print(
        "Testing record dark spell: "
        f"{dark_spell_record('Darkness', 'bats and eyeball')}"
    )


if __name__ == "__main__":
    main()