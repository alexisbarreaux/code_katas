def chop(value: int, sorted_array: list[int]) -> int:
    """
    Returns the first position of the value if found, otherwise -1.

    Recursive version
    """
    if len(sorted_array) == 0:
        return -1
    elif len(sorted_array) == 1:
        return 0 if sorted_array[0] == value else -1
    else:
        slice_point = len(sorted_array) // 2

        if sorted_array[slice_point] > value:
            return chop(value=value, sorted_array=sorted_array[:slice_point])
        else:
            result = chop(value=value, sorted_array=sorted_array[slice_point:])

            return result if result == -1 else result + slice_point
