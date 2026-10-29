
import sys

DIRECTIONS = {
    "N": {
        "weight": 1,
        "dx": 0,
        "dy": -1,
        "opposite": "S"
    },
    "E": {
        "weight": 2,
        "dx": 1,
        "dy": 0,
        "opposite": "O"
    },
    "S": {
        "weight": 4,
        "dx": 0,
        "dy": 1,
        "opposite": "N"
    },
    "O": {
        "weight": 8,
        "dx": -1,
        "dy": 0,
        "opposite": "E"
    }
}


def parsing():
    argv = sys.argv
    config = {}

    if len(argv) == 2:
        try:
            with open(argv[1], "r", encoding="utf-8") as f:
                for line_number, line in enumerate(f):
                    clean_line = line.strip()
                    if "#" in line:
                        continue
                    if not clean_line:
                        continue
                    key, value = clean_line.split("=", 1)
                    config[key] = value
        except FileNotFoundError as e:
            print(f"Unexpected error: {e}")
    return config


def build_grid(config: dict, width: int, height: int) -> list[list]:
    table = []
    while height:
        colum = [15] * width
        table.append(colum)
        height -= 1
    return table


def get_neighbors(x, y, width, height) -> list:
    """This function knows the valid neighbors"""
    valid = []

    for i in DIRECTIONS:
        nx = x + DIRECTIONS[i]["dx"]
        ny = y + DIRECTIONS[i]["dy"]
        if 0 <= nx < width and 0 <= ny < height:
            valid.append((i, (nx, ny)))
    return valid


def open_path(grid: list[list[int]], x, y, direction):
    """This function will open the actual position and the new"""

    grid[y][x] = grid[y][x] & ~ DIRECTIONS[direction]["weight"]
    nx = x + DIRECTIONS[direction]["dx"]
    ny = y + DIRECTIONS[direction]["dy"]
    opposite = DIRECTIONS[direction]["opposite"]
    grid[ny][nx] = grid[ny][nx] & ~ DIRECTIONS[opposite]["weight"]

    return grid


def dfs_algorith(grid: list[list[int]], x, y, width, height,  visited=None):
    if visited is None:
        visited = set()

    visited.add((x, y))
    for letra, (nx, ny) in get_neighbors(x, y, width, height):
        if (nx, ny) not in visited:
            open_path(grid, x, y, letra)
            dfs_algorith(grid, nx, ny, width, height, visited)
    return visited


def main():
    print("=== Maze GENERATOR ===")

    config = parsing()
    width = int(config["WIDTH"])
    height = int(config["HEIGHT"])
    grid = build_grid(config, width, height)
    dfs_algorith(grid, 0, 0, width, height)

    print(grid)


if __name__ == "__main__":

    main()
