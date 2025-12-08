import utils


def countadjacent(grid, x, y):
    if grid[x][y] == ".":
        return 9 # Default max value to prevent counting empty space
    count = 1 if x > 0 and y > 0 and grid[x-1][y-1] == "@" else 0
    count = count + 1 if y > 0 and grid [x][y-1] == "@" else count
    count = count + 1 if x < len(grid) - 1 and y > 0 and grid [x+1][y-1] == "@" else count
    count = count + 1 if x > 0 and grid [x-1][y] == "@" else count
    count = count + 1 if x < len(grid) - 1 and grid [x+1][y] == "@" else count
    count = count + 1 if x > 0 and y < len(grid[x]) - 1 and grid[x-1][y+1] == "@" else count
    count = count + 1 if y < len(grid[x]) - 1 and grid[x][y+1] == "@" else count
    count = count + 1 if x < len(grid) - 1 and y < len(grid[x]) - 1 and grid[x+1][y+1] == "@" else count
    return count


def countmoveable(grid):
    total = 0
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            total = total + 1 if countadjacent(grid, x, y) < 4 else total
    return total


def countmoveablewithremoves(grid):
    removeable = set()
    for x in range(0, len(grid)):
        for y in range(0, len(grid[x])):
            if countadjacent(grid, x, y) < 4:
                removeable.add((x, y))
    if len(removeable) > 0:
        size = len(removeable)
        for x, y in removeable:
            begin = grid[x][0:y] if y > 0 else ""
            end = grid[x][y+1:] if y < len(grid[x]) - 1 else ""
            grid[x] = begin + "." + end
        return size + countmoveablewithremoves(grid)
    return 0


if __name__ == "__main__":
    print(countmoveable(utils.file_contents("./day4input.txt")))
    print(countmoveablewithremoves(utils.file_contents("./day4input.txt")))