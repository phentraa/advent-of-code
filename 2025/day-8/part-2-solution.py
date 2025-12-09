# Solved with union-find approach + Kruskal's algorithm
# https://en.wikipedia.org/wiki/Kruskal's_algorithm

from itertools import combinations
from shared import get_junction_positions, get_edge, find_root_for, merge_circuits

if __name__ == '__main__':

    POSITIONS = get_junction_positions(test_exec=False)
    TOTAL_NODES = len(POSITIONS)
    CIRCUIT_LEADERS = list(range(TOTAL_NODES))
    CIRCUIT_SIZES = [1] * len(POSITIONS)
    
    # Generating edges in (distance, i, j) structure
    junction_edges = [ get_edge(combination[0], combination[1], POSITIONS) for combination in combinations(range(TOTAL_NODES), 2) ]
    junction_edges.sort(key=lambda edge: edge[0])

    component_count = TOTAL_NODES
    for edge in junction_edges:
        root_a = find_root_for(edge[1], CIRCUIT_LEADERS)
        root_b = find_root_for(edge[2], CIRCUIT_LEADERS) 
        
        if root_a != root_b:
            merge_circuits(root_a, root_b, CIRCUIT_LEADERS, CIRCUIT_SIZES)
            component_count -= 1
        
        if component_count == 1:
            # We reached the last edge that we have to connect
            print(f'Product of last edge X coordinates: {POSITIONS[edge[1]][0] * POSITIONS[edge[2]][0]}')
            break
