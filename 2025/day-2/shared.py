def convert(id_range:str) -> tuple[int, int]:
    """Convert range definitions into integer pairs

    Args:
        id_range (str): Two numbers separated with a '-' like '100-1234'

    Returns:
        Two integers in a tuple as start and end values of the range like (100, 1234)
    """
    
    values = id_range.split('-')
    return (int(values[0]), int(values[1]))

def get_id_ranges(test_exec: bool = False) -> list[tuple[int, int]]:
    """Read the id ranges from the test or the input file
    
    Args:
        test_exec (bool): Read from input_test.txt if True. Read from input.txt if False.

    Returns:
        list[tuple[int,int] ]: A list of start and end pairs for each range as numbers
    """
    file_name = 'input_test.txt' if test_exec else 'input.txt'
    with open(file_name, 'r') as input_file:
        return [convert(id_range) for id_range in input_file.readline().split(',')]