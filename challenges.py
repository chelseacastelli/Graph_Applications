

def depth_search(grid, row, col, x, y):
    if grid[x][y] == 0:
        return
    grid[x][y] = 0

    if x != 0:
        depth_search(grid, row, col, x - 1, y)

    if y != 0:
        depth_search(grid, row, col, x, y - 1)

    if x != row - 1:
        depth_search(grid, row, col, x + 1, y)

    if y != col - 1:
        depth_search(grid, row, col, x, y + 1)


def numIslands(grid):
    """Take in a grid of 1s (land) and 0s (water) and return the number of islands."""
    row = len(grid)
    col = len(grid)
    count = 0

    for i in range(row):
        for j in range(col):
            if grid[i][j] == 1:
                depth_search(grid, row, col, i, j)
                count += 1
    return count
