from shared import get_tile_coordinates
from itertools import combinations

def get_allowed_intervals(corners):
    """
    Returns a dict mapping row y -> list of x-intervals (start_x, end_x) that are allowed.
    """
    row_intervals = {}

    # Step 1: add green edges connecting consecutive red tiles
    for i in range(len(corners)):
        ca = corners[i]
        cb = corners[(i + 1) % len(corners)]  # wrap around

        if ca[1] == cb[1]:  # horizontal edge
            y = ca[1]
            x_start, x_end = sorted((ca[0], cb[0]))
            row_intervals.setdefault(y, []).append((x_start, x_end))
        else:  # vertical edge
            x = ca[0]
            y_start, y_end = sorted((ca[1], cb[1]))
            for y in range(y_start, y_end + 1):
                row_intervals.setdefault(y, []).append((x, x))

    # Step 2: fill interior of the loop using row scanlines
    min_y = min(c[1] for c in corners)
    max_y = max(c[1] for c in corners)

    for y in range(min_y, max_y + 1):
        if y not in row_intervals:
            continue
        # merge intervals on this row
        intervals = sorted(row_intervals[y])
        merged = []
        for start, end in intervals:
            if not merged or start > merged[-1][1] + 1:
                merged.append([start, end])
            else:
                merged[-1][1] = max(merged[-1][1], end)
        # fill gaps between leftmost and rightmost interval (interior)
        left, right = merged[0][0], merged[-1][1]
        row_intervals[y] = [(left, right)]

    return row_intervals


def is_rectangle_valid(corner_a, corner_b, allowed_intervals) -> bool:
    x_min, x_max = sorted((corner_a[0], corner_b[0]))
    y_min, y_max = sorted((corner_a[1], corner_b[1]))

    for y in range(y_min, y_max + 1):
        intervals = allowed_intervals.get(y)
        if not intervals:
            return False
        # rectangle is valid only if the interval fully covers x_min..x_max
        start, end = intervals[0]
        if start > x_min or end < x_max:
            return False

    return True


if __name__ == '__main__':

    RED_TILES = [tuple(c) for c in get_tile_coordinates(test_exec=False)]
    ALLOWED_INTERVALS = get_allowed_intervals(RED_TILES)

    maximum_area = 0
    for corner_a, corner_b in combinations(RED_TILES, 2):
        # skip rectangle if area <= current max
        width = abs(corner_a[0] - corner_b[0]) + 1
        height = abs(corner_a[1] - corner_b[1]) + 1
        if width * height <= maximum_area:
            continue

        if is_rectangle_valid(corner_a, corner_b, ALLOWED_INTERVALS):
            rectangle_area = width * height
            maximum_area = max(rectangle_area, maximum_area)

    print('Largest rectangle area:', maximum_area)
