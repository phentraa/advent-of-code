# Solved with union-find approach
from itertools import combinations
from shared import get_junction_positions, get_edge, find_root_for, merge_circuits

if __name__ == '__main__':

    POSITIONS = get_junction_positions(test_exec=False)
    CIRCUIT_LEADERS = list(range(len(POSITIONS)))
    CIRCUIT_SIZES = [1] * len(POSITIONS)
    
    # Generating edges in (distance, i, j) structure
    junction_edges = [ get_edge(combination[0], combination[1], POSITIONS) for combination in combinations(range(len(POSITIONS)), 2) ]
    junction_edges.sort(key=lambda edge: edge[0])

    for i in range(1000):
        root_a = find_root_for(junction_edges[i][1], CIRCUIT_LEADERS)
        root_b = find_root_for(junction_edges[i][2], CIRCUIT_LEADERS) 
        
        if root_a != root_b:
            merge_circuits(root_a, root_b, CIRCUIT_LEADERS, CIRCUIT_SIZES)
    
    NEW_CIRCUIT_SIZES = [ CIRCUIT_SIZES[leader_id] for leader_id in set(CIRCUIT_LEADERS)]     
    CIRCUIT_SIZES.sort(reverse=True)

    result = CIRCUIT_SIZES[0] * CIRCUIT_SIZES[1] * CIRCUIT_SIZES[2]
    print('Result: ', result)
