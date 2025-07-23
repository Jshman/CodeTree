def triangle(y, x, grid):
    S = 0
    for i in range(2):
        for j in range(2):
            S += grid[y+i][x+j]
    ans = -1
    for i in range(2):
        for j in range(2):
            ans = max(ans, S - grid[y+i][x+j])
    return ans

def line_row(y, x, grid):
    row = 0
    for i in range(3):
        row += grid[y+i][x]
    return row

def line_col(y, x, grid):
    col = 0
    for i in range(3):
        col += grid[y][x+i]
    return col


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

ans = 0
# row
for i in range(n-2):
    for j in range(m):
        ans = max(ans, line_row(i, j, grid))

for i in range(n):
    for j in range(m-2):
        ans = max(ans, line_col(i, j, grid))

for i in range(n-1):
    for j in range(m-1):
        ans = max(ans, triangle(i,j,grid))

print(ans)