
from collections import deque
from graph import Graph


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
    rows = len(grid)
    cols = len(grid[0])

    time_to_rot = 0
    queue = deque()

    for row in range(rows):
        for col in range(cols):
            # position = (row * rows) + col
            position = grid[row][col]

            # add rotted oranges to queue with T minus 0
            if position == 2:
                queue.append((row, col, 0))

    while queue:
        row, col, tminus = queue.popleft()

        if tminus > time_to_rot:
            time_to_rot = tminus

        # infect neighbors
        north = row - 1
        south = row + 1
        west = col - 1
        east = col + 1

        if row > 0 and grid[north][col] == 1:
            grid[north][col] = 2
            queue.append((north, col, tminus + 1))
        if row < rows - 1 and grid[south][col] == 1:
            grid[south][col] = 2
            queue.append((south, col, tminus + 1))
        if col > 0 and grid[row][west] == 1:
            grid[row][west] = 2
            queue.append((row, west, tminus + 1))
        if col < cols - 1 and grid[row][east] == 1:
            grid[row][east] = 2
            queue.append((row, east, tminus + 1))

    # if any fresh oranges remain after contagion(isolated)
    if [y for x in grid for y in x if y == 1]:
        return -1

    return time_to_rot


def courseOrder(numCourses, prerequisites):
    """Return a course schedule according to the prerequisites provided."""
    graph = Graph(is_directed=True)

    course = [graph.add_vertex(each) for courses in prerequisites for each in courses]

    if numCourses != len(graph.get_vertices()):
        return []

    for each in prerequisites:
        graph.add_edge(each[1], each[0])

    return graph.topological_sort()


def wordLadderLength(beginWord, endWord, wordList):
    """Return the length of the shortest word chain from beginWord to endWord, using words from wordList."""
    pass



