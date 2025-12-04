ADJACENT_POSITIONS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0,1),
    (1, -1), (1, 0), (1, 1)
]


def count_adjacent_rolls(grid: list[str], row: int, column: int) -> int:
    """
    Counts the adjacent rolls from a given position.
    
    Args:
        grid (list[str]): The grid of rolls
        row (int): The row where the center roll can be found
        column (int): The column where the center roll can be found
    
    Returns: 
        The count of adjacents rolls
    """
    count = 0

    for position in ADJACENT_POSITIONS:
        if grid[row + position[0]][column + position[1]] == '@':
            count += 1
    
    return count


def get_extended_roll_grid(test_exec: bool = False):
    """
    Reads the input that defines the datagrid of the rolls then wrap it around with empty placeholders.

    Args:
        test_exec (bool): Reads the input_test.txt if True. Else reads the input.txt. 

    Returns:
        grid (list[str]): The wrapped roll grid
    """
    file_name = 'input_test.txt' if test_exec else 'input.txt'
   
    with open(file_name, 'r') as f:
        grid = ['.' + line.strip() + '.' for line in f.readlines()]
        width = len(grid[0])

        grid.insert(0, '.' * width)
        grid.append('.' * width)

        return grid