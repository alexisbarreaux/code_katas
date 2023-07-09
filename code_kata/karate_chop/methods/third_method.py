from dataclasses import dataclass


@dataclass
class ArraySearcherClass:
    value: int
    sorted_array: list[int]
    offset: int = 0

    def get_midpoint(self):
        return len(self.sorted_array) // 2

    def check_midpoint(self):
        midpoint = self.get_midpoint()
        if self.sorted_array[midpoint] == self.value:
            return 0
        elif self.sorted_array[midpoint] < self.value:
            return 1
        else:
            return -1

    def final_check(self):
        if len(self.sorted_array) == 1 and self.sorted_array[0] == self.value:
            return self.offset
        else:
            return -1

    def slice_left(self):
        self.sorted_array = self.sorted_array[: self.get_midpoint()]

    def slice_right(self):
        self.offset += self.get_midpoint() + 1
        self.sorted_array = self.sorted_array[(self.get_midpoint()) + 1 :]

    def done_searching(self):
        return len(self.sorted_array) <= 1


def chop(value: int, sorted_array: list[int]) -> int:
    """
    Returns the first position of the value if found, otherwise -1.

    Class version
    """
    searcher = ArraySearcherClass(value=value, sorted_array=sorted_array)

    while not searcher.done_searching():
        if (check_value := searcher.check_midpoint()) == 0:
            return searcher.get_midpoint() + searcher.offset
        elif check_value == -1:
            searcher.slice_left()
        else:
            searcher.slice_right()
    else:
        return searcher.final_check()
