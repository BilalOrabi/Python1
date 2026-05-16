def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients

    allowed: list[str] = light_spell_allowed_ingredients()
    lowered_ingredients: str = ingredients.lower()

    for ingredient in allowed:
        if ingredient in lowered_ingredients:
            return f"{ingredients} - VALID"

    return f"{ingredients} - INVALID"