def get_junction_positions(test_exec: bool = False):
    file_name = 'input_test.txt' if test_exec else 'input.txt'

    coordinates = []
    with open(file_name, 'r') as f:
        for line in f:
            line = line.strip()
            values = line.split(',')

            coordinates.append([ int(value) for value in values ])

    return coordinates


def get_edge(i, j, positions) -> tuple:
    p1 = positions[i]
    p2 = positions[j]

    return (
        (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2,
        i,
        j
    )


def find_root_for(node: int, leaders: list) -> int:
    """Path compression solved with recursion"""
    if leaders[node] != node:
        leaders[node] = find_root_for(leaders[node], leaders)
    return leaders[node]


def merge_circuits(c1, c2, leaders, sizes):
    size_1 = sizes[c1]
    size_2 = sizes[c2]

    if size_1 >= size_2:
        leaders[c2] = c1
        sizes[c1] += size_2
    else: 
        leaders[c1] = c2
        sizes[c2] += size_1