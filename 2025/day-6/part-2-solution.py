from shared import get_problems_and_operators_part_2

def product(l: list[int]):
    """Multiply the elements in a list with each other
    
    Args:
        l (list[int]): A list containing numbers
    
    Returns:
        The product of each number in the list
    """
    result = 1
    for e in l:
        result = result * e
    return result


if __name__ == '__main__':
    problems, operators = get_problems_and_operators_part_2(test_exec=False)
    
    grand_total = 0

    # Get vertical numbers for each problem
    for problem_index, problem in enumerate(problems):
        
        max_length = max(len(s) for s in problem)
        vertical_numbers = []
        
        # Iterates through char-by-char on all string represented numbers in a problem
        # and concatenate their chars. Then store them as an integer. 
        for i in range(max_length):
            vertical_number = ''
            for number in problem:
                vertical_number += number[i]

            vertical_numbers.append(int(vertical_number))

        # Summation of the gotten vertical numbers with different operators
        # problem_index helps to determine the related operator to the problem
        # The start value of total depends on the actual operator.
        total = 0 if operators[problem_index] == '+' else 1

        if operators[problem_index] == '+':
            total += sum(vertical_numbers)
        else:
            total *= product(vertical_numbers)

        grand_total += total

    print('Grand Total:', grand_total)