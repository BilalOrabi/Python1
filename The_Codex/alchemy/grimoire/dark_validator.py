from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed: list[str] = dark_spell_allowed_ingredients()
    lowered_ingredients: str = ingredients.lower()

    for ingredient in allowed:
        if ingredient in lowered_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"