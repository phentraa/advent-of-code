def get_tile_coordinates(test_exec: bool = False) -> list[list[int]]:
    file_name = 'input_test.txt' if test_exec else 'input.txt'

    with open(file_name, 'r') as f:
        return [ [int(x) for x in line.split(',')] for line in f ]

