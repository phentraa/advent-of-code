from shared import get_id_ranges

def is_repetitive(actual_id: int) -> bool:
    """Decides that the id has been built by repetitive pattern or not.
    Example
    1. Getting the id (824824824)
    2. Duplicate it (824824824824824824)
    3. Remove first and last elements (2482482482482482)
    4. If the original id is part of the modified id, then it is repetitive. (824824824 in 2482482482482482 is True)

    Args:
        actual_id (int): The id that has to be examined

    Returns:
        bool : True if the pattern is repetitive.
    """
    value = str(actual_id)
    return value in (value + value)[1:-1]


if __name__ == '__main__':
    
    result = 0
    
    for actual_range in get_id_ranges(test_exec=False):
        start, end = actual_range

        for actual_id in range(start, end + 1):
            if is_repetitive(actual_id):
                result += actual_id

    print('Result: ', result)