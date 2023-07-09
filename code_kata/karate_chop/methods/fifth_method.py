def chop(value: int, sorted_array: list[int]) -> int:
    """
    Returns the first position of the value if found, otherwise -1.

    Pointer version
    """
    if len(sorted_array) == 0:
        return -1

    pre_previous_pointer = 0
    previous_pointer = 0
    current_pointer = len(sorted_array) // 2
    while (
        current_pointer != previous_pointer and current_pointer != pre_previous_pointer
    ):
        pre_previous_pointer = previous_pointer
        previous_pointer = current_pointer

        if sorted_array[current_pointer] == value:
            return current_pointer
        elif sorted_array[current_pointer] < value:
            if len(sorted_array[current_pointer + 1 :]) == 1:
                current_pointer += 1
            else:
                current_pointer += len(sorted_array[current_pointer + 1 :]) // 2
        else:
            if len(sorted_array[:current_pointer]) == 1:
                current_pointer -= 1
            else:
                current_pointer -= len(sorted_array[:current_pointer]) // 2
    else:
        if sorted_array[current_pointer] == value:
            return current_pointer
        else:
            return -1
