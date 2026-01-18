def ft_count_harvest_iterative() -> None:
    harvest_days: int = int(input("Days until harvest: "))
    for current_day in range(1, harvest_days + 1):
        print(f"Day {current_day}")
    print("Harvest time!")
