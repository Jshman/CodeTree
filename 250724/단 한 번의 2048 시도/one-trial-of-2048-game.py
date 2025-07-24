# Read 4x4 grid
grid = [list(map(int, input().split())) for _ in range(4)]

# Read direction
dir = input()


def LEFT(grid):
    leng = len(grid)
    for i in range(leng):
        row = grid[i]
        for j in range(leng):
            for k in range(j+1, leng):
                if row[j] == row[k]:
                    row[j] *= 2
                    row[k] = 0
                    break
                elif row[j] != row[k] and row[k] > 0:
                    break
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
        for j in range(leng-1, -1, -1):
            for k in range(j-1, -1, -1):
                if row[j] == row[k]:
                    row[j] *= 2
                    row[k] = 0
                    break
                elif row[j] != row[k] and row[k] > 0:
                    break
                
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
        for j in range(leng):
            for k in range(j+1, leng):
                if col[j] == col[k]:
                    col[j] *= 2
                    col[k] = 0
                    break
                elif col[j] != col[k] and col[k] > 0:
                    break
        # 0으로 초기화
        for j in range(leng):
            grid[j][i] = 0

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

        for j in range(leng-1, -1, -1):
            for k in range(j-1, -1, -1):
                if col[j] == col[k]:
                    col[j] *= 2
                    col[k] = 0
                    break
                elif col[j] != col[k] and col[k] > 0:
                    break

        # 0으로 초기화
        for j in range(leng):
            grid[j][i] = 0

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