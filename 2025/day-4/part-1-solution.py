from shared import get_extended_roll_grid, count_adjacent_rolls

if __name__ == '__main__':
    
    grid = get_extended_roll_grid(test_exec=False)
    
    accessible_roll_count = 0
    for i, row in enumerate(grid[1:-1], start=1):
        for j, element in enumerate(row):
            if element == '.':
                continue
            if count_adjacent_rolls(grid, i, j) < 4:
                accessible_roll_count += 1
    
    print('Accessible rolls:', accessible_roll_count)



