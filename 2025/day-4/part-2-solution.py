from shared import get_extended_roll_grid, count_adjacent_rolls

def get_accessible_roll_coordinates(grid: list[str]) -> list[tuple]:
    """
    Collects the coordinates of all accessible rolls in a grid
    
    :param grid: The roll grid where the function has to look
    :type grid: list[str]
    :return: A list of coordinates of the accessible rolls
    :rtype: list[tuple[Any, ...]]
    """

    accessible_roll_coordinates: list[tuple] = []

    for i, row in enumerate(grid[1:-1], start=1):
        for j, element in enumerate(row):
            if element == '.':
                continue
            if count_adjacent_rolls(grid, i, j) < 4:
                accessible_roll_coordinates.append((i, j))
    
    return accessible_roll_coordinates


def replace_char_at_position(original: str, position: int, new_char: str) -> str:
    """
    Replaces a character in a string on a given position
    
    :param original: The original string
    :type original: str
    :param position: The position of the character that has to be replaced
    :type position: int
    :param new_char: The character that will replace the old one
    :type new_char: str
    :return: The new string with the replaced character
    :rtype: str
    """
    mutable = list(original)
    mutable[position] = new_char
    return ''.join(mutable)


def remove_accessible_rolls(grid: list[str], coordinates: list[tuple]):
    """
    Replaces all the '@' roll marks in the grid with a '.' on the given coordinates

    :param grid: The whole roll grid 
    :type grid: list[str]
    :param coordinates: The exact locations of the accessible rolls
    :type coordinates: list[tuple]
    """
    for c in coordinates:
        grid[c[0]] = replace_char_at_position(
            grid[c[0]], c[1], '.'
        )


if __name__ == '__main__':
  
    grid = get_extended_roll_grid(test_exec=False)

    removed_total = 0
    while coordinates := get_accessible_roll_coordinates(grid):
        remove_accessible_rolls(grid, coordinates)
        removed_total += len(coordinates)
    
    
    print('Removed:', removed_total)



