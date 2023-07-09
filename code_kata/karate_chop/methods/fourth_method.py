def chop(value: int, sorted_array: list[int]) -> int:
    """
    Returns the first position of the value if found, otherwise -1.

    Pop version
    """
    offset = 0

    while len(sorted_array) > 0:
        midpoint = len(sorted_array) // 2
        if sorted_array[midpoint] == value:
            return midpoint + offset
        elif midpoint == 0:
            return -1
        elif sorted_array[midpoint] < value:
            for _ in range(midpoint + 1):
                sorted_array.pop(0)
                offset += 1
        else:
            for _ in range(len(sorted_array) - midpoint):
                sorted_array.pop()
    else:
        return -1
