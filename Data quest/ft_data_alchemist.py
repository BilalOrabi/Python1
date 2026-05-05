import random


def main() -> None:
    players = [
        "Messi",
        "ronaldo",
        "Neymar",
        "kylian",
        "Mohammed",
        "harry",
        "Kevin",
        "virgil"
    ]

    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {players}")

    capitalized_list = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_list}")

    capitalized_names_only = [player for player in players if player.istitle()]
    print(f"New list of capitalized names only: {capitalized_names_only}")

    print()

    players_dict = {
        player: random.randint(1, 999) for player in capitalized_list}

    players_avg = sum(
        players_dict.values()) / len(players_dict) if players_dict else 0

    print(f"Score dict: {players_dict}")
    print(f"Score average is {players_avg:.2f}")

    players_high_scores = {
        player: score
        for player, score in players_dict.items()
        if score > players_avg
    }

    print(f"High scores: {players_high_scores}")


if __name__ == "__main__":
    main()
