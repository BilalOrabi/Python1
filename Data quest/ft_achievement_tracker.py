import random


def gen_player_achievements() -> set[str]:
    all_achievements = [
        "PENTAKIIIIIIIIL!!",
        "Jungle Diff",
        "Lane Domination",
        "Top Performer",
        "The Jukes!",
        "Global Defense System",
        "TY for Leash",
        "Farm Champs not Camps",
        "Clutch Steal",
        "Pain Prescriber",
        "Fun with Friends",
        "KDA Player",
        "Fury of the North",
        "Final Boss Faker",
        "The Unforgiven",
        "The River King",
        "Dragon in Disguise",
        "Elegant",
        "G.O.A.T.",
        "Playmaker",
    ]

    count = random.randint(3, 6)
    picked = random.sample(all_achievements, count)
    return set(picked)


def main() -> None:

    all_achievements = [
        "PENTAKIIIIIIIIL!!",
        "Jungle Diff",
        "Lane Domination",
        "Top Performer",
        "The Jukes!",
        "Global Defense System",
        "TY for Leash",
        "Farm Champs not Camps",
        "Clutch Steal",
        "Pain Prescriber",
        "Fun with Friends",
        "KDA Player",
        "Fury of the North",
        "Final Boss Faker",
        "The Unforgiven",
        "The River King",
        "Dragon in Disguise",
        "Elegant",
        "G.O.A.T.",
        "Playmaker",
    ]
    all_achievements_set = set(all_achievements)
    print("=== Achievement Tracker System ===\n")

    player1 = gen_player_achievements()
    player2 = gen_player_achievements()
    player3 = gen_player_achievements()
    player4 = gen_player_achievements()

    print(f"\nPlayer Bilal: {player1}")
    print(f"\nPlayer Mohammad: {player2}")
    print(f"\nPlayer Omar: {player3}")
    print(f"\nPlayer Noor: {player4}")

    all_distinct_achievements = player1 | player2 | player3 | player4

    common_achievements = player1 & player2 & player3 & player4

    only_p1 = player1 - (player2 | player3 | player4)
    only_p2 = player2 - (player1 | player3 | player4)
    only_p3 = player3 - (player1 | player2 | player4)
    only_p4 = player4 - (player1 | player2 | player3)

    missing_p1 = all_achievements_set - player1
    missing_p2 = all_achievements_set - player2
    missing_p3 = all_achievements_set - player3
    missing_p4 = all_achievements_set - player4

    print(f"\nAll distinct achievements: {all_distinct_achievements}")

    print(f"\nCommon achievements: {common_achievements}")

    print(f"\nOnly Bilal has: {only_p1}")
    print(f"Only Mohammad has: {only_p2}")
    print(f"Only Omar has: {only_p3}")
    print(f"Only Noor has: {only_p4}")

    print(f"Bilal is missing: {missing_p1}")
    print(f"Mohammad is missing: {missing_p2}")
    print(f"Omar is missing: {missing_p3}")
    print(f"Noor is missing: {missing_p4}")


if __name__ == "__main__":
    main()
