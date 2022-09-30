def uncommon_cities(my_cities, other_cities):
    """Compare my_cities and other_cities and return the number of different
    cities between the two"""
    diff = list(
        list(set(my_cities) - set(other_cities))
        + list(set(other_cities) - set(my_cities))
    )
    return len(diff)


uncommon_cities(
    ["Rome", "Paris", "Madrid", "Chicago", "Seville", "Berlin"],
    ["Paris", "Boston", "Sydney", "Madrid", "Moscow", "Lima"],
)  # 8
