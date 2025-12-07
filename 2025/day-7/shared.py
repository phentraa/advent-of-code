def get_manifest(test_exec: bool = False):
    file_name = 'input_test.txt' if test_exec else 'input.txt'

    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_index_of_char_in_row(char: str, row: str):
    pass