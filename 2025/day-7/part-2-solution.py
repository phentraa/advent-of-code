from functools import lru_cache
from shared import get_manifest

@lru_cache(maxsize=None)
def visit_timeline(level: int, position: int) -> int:
    # Out of horizontal bounds
    if position < 0 or position >= width:
        return 0

    # Reached the bottom → one complete timeline
    if level == height - 1:
        return 1

    if manifest[level][position] == '^':
        return (
            visit_timeline(level + 1, position - 1) +
            visit_timeline(level + 1, position + 1)
        )
    else:
        return visit_timeline(level + 1, position)


if __name__ == "__main__":
    manifest = get_manifest(test_exec=False)

    # First row contains 'S'
    start_position = manifest[0].find('S')

    # We start "moving" from the row AFTER S
    manifest = manifest[1:]

    height = len(manifest)
    width = len(manifest[0])

    timeline_count = visit_timeline(0, start_position)

    print("Timeline count:", timeline_count)
