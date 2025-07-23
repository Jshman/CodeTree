# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()

# Please write your code here.
def LEFT(grid):
    leng = len(grid)
    for i in range(leng):
        row = grid[i]
        for j in range(leng-1):
            if row[j] == row[j+1]:
                row[j] *= 2
                row[j+1] = 0
        grid[i] = [0] * leng
        idx, j = 0, 0
        while j < leng:
            if row[j] > 0:
                grid[i][idx] = row[j]
                idx += 1
            j += 1
    return grid

def RIGHT(grid):
    leng = len(grid)
    for i in range(leng):
        row = grid[i]
        for j in range(leng-1, 0, -1):
            if row[j] == row[j-1]:
                row[j] *= 2
                row[j-1] = 0
        grid[i] = [0] * leng
        idx, j = leng-1, leng-1
        while j >= 0:
            if row[j] > 0:
                grid[i][idx] = row[j]
                idx -= 1
            j -= 1
    return grid

def UP(grid):
    leng = len(grid)
    for i in range(leng):
        col = [grid[k][i] for k in range(leng)]
        for j in range(leng-1):
            if col[j] == col[j+1]:
                col[j] *= 2
                col[j+1] = 0

        idx, j = 0, 0
        while j < leng:
            if col[j] > 0:
                grid[idx][i] = col[j]
                idx += 1
            j += 1

        for j in range(idx, leng):
            grid[j][i] = 0

    return grid

def DOWN(grid):
    leng = len(grid)
    for i in range(leng):
        col = [grid[k][i] for k in range(leng)]

        for j in range(leng-1, 0, -1):
            if col[j] == col[j-1]:
                col[j] *= 2
                col[j-1] = 0

        idx, j = leng-1, leng-1
        while j >= 0:
            if col[j] > 0:
                grid[idx][i] = col[j]
                idx -= 1
            j -= 1

        for j in range(0, idx):
            grid[j][i] = 0
    return grid

if dir == 'L':
    grid = LEFT(grid)
elif dir == 'R':
    grid = RIGHT(grid)
elif dir == 'U':
    grid = UP(grid)
else:
    grid = DOWN(grid)

for elem in grid:
    print(*elem)