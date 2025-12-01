actual_dial_position = 50

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

def get_new_dial_position(actual, rotation):
    """
    Computes the new position of the dial after one rotation

    Args:
        actual (int): The actual dial position
        rotation (int): A rotation distance as a positive or negative number
    
    Returns:
        int: The new dial position
    """
    result = actual + (rotation % 100) # Expecting for more than 1 rounds on the dial
    
    if result < 0:
        result = 100 + result
    elif result > 99:
        result = result - 100

    return result


if __name__ == '__main__':
    rotations = None
    with open('input.txt', 'r') as input:
        rotations = [rotation_to_int(r) for r in input.readlines()]
    
    reached_zero_count = 0

    # print(rotations)
    for rotation in rotations:
        # print('Actual dial position: ', actual_dial_position)

        actual_dial_position = get_new_dial_position(
            actual_dial_position,
            rotation
        )
        
        if actual_dial_position == 0:
            reached_zero_count += 1

    # print('Actual dial position: ', actual_dial_position)

    print('Reached 0: ', reached_zero_count)    
