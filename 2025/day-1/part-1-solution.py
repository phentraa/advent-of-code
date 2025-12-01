from shared import read_rotations_from_input
actual_dial_position = 50

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
    
    
    reached_zero_count = 0

    # print(rotations)
    for rotation in read_rotations_from_input(test_exec=True):
        # print('Actual dial position: ', actual_dial_position)

        actual_dial_position = get_new_dial_position(
            actual_dial_position,
            rotation
        )
        
        if actual_dial_position == 0:
            reached_zero_count += 1

    # print('Actual dial position: ', actual_dial_position)

    print('Reached 0: ', reached_zero_count)    
