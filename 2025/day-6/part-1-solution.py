from shared import get_problems_and_operators

if __name__ == '__main__':
    problems, operators = get_problems_and_operators(test_exec=False)

    full_length = len(operators)
    grand_total = 0

    for index in range(full_length):
        
        operator = operators[index]
        total = 0 if operator == '+' else 1

        for problem in problems:
            
            if operator == '+':
                total += int(problem[index])
            elif operator == '*':
                total *= int(problem[index])
            else:
                raise ValueError(f'Unexpected operator: {operator}')
        
        grand_total += total

    print('Grand Total:', grand_total)