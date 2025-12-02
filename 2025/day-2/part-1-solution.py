from shared import get_id_ranges

if __name__ == '__main__':
    
    result = 0
    
    for actual_range in get_id_ranges(test_exec=False):
        start, end = actual_range

        for actual_id in range(start, end+1):
            id_as_string = str(actual_id)
            center_position = len(id_as_string) // 2
            
            if id_as_string[:center_position] == id_as_string[center_position:]:
                result += actual_id       

    print('Result: ', result)
