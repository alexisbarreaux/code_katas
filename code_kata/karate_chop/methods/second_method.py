def chop(value: int, sorted_array: list[int]) -> int:
    """
    Returns the first position of the value if found, otherwise -1.

    Iterative version
    """
    first_index = 0
    last_index = len(sorted_array) - 1

    while first_index < last_index:
        midpoint = len(sorted_array) // 2
        if sorted_array[midpoint] == value:
            return midpoint
        elif sorted_array[midpoint] < value:
            first_index = midpoint
        else:
            last_index = midpoint
    else:
        return -1
