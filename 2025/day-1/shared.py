def rotation_to_int(rotation: str) -> int:
    """Convert rotation into a negative or positive integer.

    Args:
        rotation (str): The direction and distance of the rotation, 
                        consisting of an 'L' or 'R' character followed by an integer.

    Returns:
        int: A negative integer if the string starts with 'L', 
             and a positive integer if it starts with 'R'.
    """

    number = int(rotation[1:])
    return number if rotation[0] == 'R' else -number


def read_rotations_from_input(test_exec : bool = False) -> list[int]:
    """Reads the input input lines then converts them into negative or positive integers

    Args:
        test_exec (bool): Reads input_test.txt if true. Reads input.txt if false.

    Returns:
        list[int]: A list of integers as rotations
    """
    filename = 'input_test.txt' if test_exec else 'input.txt'
    with open(filename, 'r') as input:
        return [rotation_to_int(r) for r in input.readlines()]