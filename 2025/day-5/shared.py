class Interval:
    """Represents a range of numbers."""
    start: int
    end: int

    def __init__(self, start: int, end: int) -> None:
        """Initializes an Interval object."""
        self.start = start
        self.end = end

    
    def __str__(self) -> str:
        """Returns a string representation of the interval."""
        return f'{self.start} - {self.end}'

    
    def number_of_integers(self) -> int:
        """Calculates the number of integers in the interval."""
        return self.end + 1 - self.start
    

    


def transform_range_string(s: str) -> Interval:
    """Converts a string in the format 'start-end' to an Interval object."""
    endpoints = s.split('-')
    return Interval(int(endpoints[0]), int(endpoints[1]))



def read_input_part_1(test_exec: bool = False) -> tuple[list, list]:
    """
    Reads the input for part 1 of the puzzle.

    Args:
        test_exec: Whether to use the test input file.

    Returns:
        A tuple containing two lists: id_ranges and ids.
    """
    file_name = 'input_test.txt' if test_exec else 'input.txt'

    id_ranges = []
    ids = []
    store_in_ranges_list = True

    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                store_in_ranges_list = False
                continue
            if store_in_ranges_list:
                id_ranges.append(line)
            else:
                ids.append(line)

    return id_ranges, ids


def read_input_part_2(test_exec: bool = False) -> list:
    """
    Reads the input for part 2 of the puzzle.

    Args:
        test_exec: Whether to use the test input file.

    Returns:
        A sorted list of Interval objects.
    """
    file_name = 'input_test.txt' if test_exec else 'input.txt'

    id_ranges = []

    with open(file_name, 'r') as f:
        for line in f:
            
            line = line.strip()
            
            if line == '':
                break
            
            id_ranges.append(
                transform_range_string(line)
            )

    return sorted(id_ranges, key=lambda interval: interval.start)