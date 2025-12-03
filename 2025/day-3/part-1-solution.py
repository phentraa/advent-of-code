from shared import get_banks_from_input

def get_max_joltage_from(bank):
    """
    Finds the largest, two digit integer in the given bank
    
    :param bank: The original input line that represents a bank of batteries
    :type bank: str
    :return: The largest, two digit integer that can be found in the given bank
    :rtype: int
    """
    bank = bank.strip()
    max_joltage = 0
    for i in range(len(bank)):
        for j in range(i+1, len(bank)):
            joltage = int(bank[i] + bank[j])
            if joltage > max_joltage:
                max_joltage = joltage
    return max_joltage


if __name__ == '__main__':
    
    total_joltage = 0
    for bank in get_banks_from_input(test_exec=False):
        total_joltage += get_max_joltage_from(bank)
    print('Total: ', total_joltage)