def get_problems_and_operators(test_exec: bool = False) -> tuple[list[list], list[str]]:
    """Reads and processes the input file for part 1.

    Args:
        test_exec: Whether to use the test input file.
    
    Returns:
        returns with separated lists of problems and operators
    
    """
    
    file_name = 'input_test.txt' if test_exec else 'input.txt'
    problems: list[list] = []

    with open(file_name, 'r') as f:
        
        for line in f:
            problems.append(
                [x.strip() for x in line.split(' ') if x not in ['', '\n']]
            )
    
    operators = problems[-1]

    return problems[:-1], operators


def get_problems_and_operators_part_2(test_exec: bool = False) -> tuple:
    """Reads and processes the input file for part 2. 
    Splits the input strings at column separators, leaving the preceiding or following whitespaces as part of the number.

    Args:
        test_exec: Whether to use the test input file.
    
    Returns:
        returns with separated lists of problems and operators in reversed order
    
    """
    
    file_name = 'input_test.txt' if test_exec else 'input.txt'
    problems: list[str] = []

    with open(file_name, 'r') as f:
        
        for line in f:
            problems.append(line)
    
    # Clean and store the values from the last line as operators
    operators = [x for x in problems[-1].split(' ') if x != '']
    operators.reverse()

    # Removing last line from problems
    problems = problems[:-1]

    # Splitting rows on column borders by examining the string char-by-char from right to left
    splitted_problems = []
    end = len(problems[0]) - 1

    for index in range(end,-1,-1):
        # If all row has a whitespace char on the given index the it is a column border
        # In this case I have to append the preceiding characters from the current index to the last column border
        # to the result list for each row.
        if all(row[index] == ' ' for row in problems):
            splitted_problems.append(
                [row[index+1:end] for row in problems]
            )
            end = index

    # I also have to add the last column values for each row
    splitted_problems.append(
                [row[0:end] for row in problems]
            )
    

    return splitted_problems, operators