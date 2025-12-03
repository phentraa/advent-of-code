def get_banks_from_input(test_exec=False):
    """Read the id ranges from the test or the input file
    
    Args:
        test_exec (bool): Read from input_test.txt if True. Read from input.txt if False.

    Returns:
        list[tuple[int,int] ]: A list of start and end pairs for each range as numbers
    """
    file_name = 'input_test.txt' if test_exec else 'input.txt'
    with open(file_name, 'r') as input_file:
        return input_file.readlines()
