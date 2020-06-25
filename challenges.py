

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


def timeToRot(grid):
    """
    Take in a grid of numbers, where 0 is an empty space, 1 is a fresh orange, and 2 is a rotten
    orange. Each minute, a rotten orange contaminates its 4-directional neighbors. Return the number
    of minutes until all oranges rot.
    """
    pass


def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    pass


def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass



