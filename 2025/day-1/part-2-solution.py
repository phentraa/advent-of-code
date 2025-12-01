from shared import read_rotations_from_input

ACTUAL_DIAL_POSITION = 50
REACHED_ZERO_COUNTER = 0

def get_new_dial_position(actual_position, rotation):
    """
    Computes the new position of the dial after one rotation

    Args:
        actual (int): The actual dial position
        rotation (int): A rotation distance as a positive or negative number
    
    Returns:
        int: The new dial position
    """
    global REACHED_ZERO_COUNTER 
    
    full_round_count = abs(rotation) // 100
    REACHED_ZERO_COUNTER += full_round_count

    disposable_part = full_round_count * 100
    rotation = rotation - disposable_part if rotation > 0 else rotation + disposable_part

    new_position = actual_position + rotation

    if new_position == 0:
        REACHED_ZERO_COUNTER += 1
    elif new_position < 0:
        new_position = 100 + new_position
        if new_position + abs(rotation) > 100:
            REACHED_ZERO_COUNTER += 1
    elif new_position > 99:
        new_position = new_position - 100
        REACHED_ZERO_COUNTER += 1
    
    return new_position


if __name__ == '__main__':
    
    for rotation in read_rotations_from_input(test_exec=False):
        
        ACTUAL_DIAL_POSITION = get_new_dial_position(
            ACTUAL_DIAL_POSITION,
            rotation
        )

    print('Reached 0: ', REACHED_ZERO_COUNTER)    
