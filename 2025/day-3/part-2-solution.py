from shared import get_banks_from_input

def get_maximum_joltage_from(bank: str) -> int:
    """
    Solved with a monotonic decreasing stack.
    I store the numbers in the bank sequentially in the result stack.
    I always remove smaller numbers than the current one until I reach the required length.
    
    :param bank: The original input line that represents a bank of batteries
    :type bank: str
    :return: The largest integer that we can found in the given bank
    :rtype: int
    """
    bank = bank.strip()
    drop = len(bank) - 12
    result_stack = []

    for number in bank:
        while drop > 0 and result_stack and result_stack[-1] < number:
            result_stack.pop()
            drop -= 1
        result_stack.append(number)
    
    return int(''.join(result_stack[:12]))
        

if __name__ == '__main__':
    
    total_joltage = 0
    for bank in get_banks_from_input(test_exec=False):
        total_joltage += get_maximum_joltage_from(bank)

    print('Total:', total_joltage)