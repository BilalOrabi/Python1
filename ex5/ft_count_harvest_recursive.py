def ft_count_harvest_recursive(day=1, harvest_days=None) -> None:
    if harvest_days is None:
        harvest_days: int = int(input("Days until harvest: "))
    if day <= harvest_days:
        print(f"Day {day}")
        ft_count_harvest_recursive(day + 1, harvest_days)
    else:
        print("Harvest time!")
