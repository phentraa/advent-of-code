from shared import read_input_part_1, transform_range_string

if __name__ == '__main__':
    id_ranges, ids = read_input_part_1(test_exec=True)

    fresh_count = 0
    for id in ids:
        for id_range in id_ranges:
            interval = transform_range_string(id_range)

            if interval.start <= int(id) <= interval.end:
                fresh_count += 1
                break

    print('Fresh:', fresh_count)