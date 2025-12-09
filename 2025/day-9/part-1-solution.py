from shared import get_tile_coordinates
from itertools import combinations

if __name__ == '__main__':
    RECTANGLE_CORNERS = combinations(get_tile_coordinates(test_exec=False), 2)

    maximum_area = 0
    for corners in RECTANGLE_CORNERS:
        ca = corners[0]
        cb = corners[1]

        width = abs(ca[0] - cb[0]) + 1
        height = abs(ca[1] - cb[1]) + 1

        rectangle_area = width * height

        maximum_area = max(rectangle_area, maximum_area)
    
    print('Largest rectangle area: ', maximum_area)