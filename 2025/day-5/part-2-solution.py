from shared import read_input_part_2

if __name__ == '__main__':
    id_ranges = read_input_part_2(test_exec=False)

    disjoint_ranges = []

    for id_range in id_ranges:

        if not disjoint_ranges:
            disjoint_ranges.append(id_range)
        else:
            previous_interval = disjoint_ranges[-1]
            if previous_interval.end >= id_range.start:
                previous_interval.end = max(previous_interval.end, id_range.end)
            else:
                disjoint_ranges.append(id_range)
    
    counter = 0
    for dr in disjoint_ranges:
        counter += dr.number_of_integers()
    
    print('Count:', counter)