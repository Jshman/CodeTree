def in_range(y, x, h, w):
    return 0<=y and y<h and 0<=x and x<w

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dyxs = [(0, 1), (1, 0)]
stk = [(0, 0)]
while stk:
    y, x = stk.pop()
    grid[y][x] = -1
    if y == n-1 and x == m-1:
        break
    for dy, dx in dyxs:
        ny, nx = y+dy, x+dx
        if in_range(ny, nx, n, m) and grid[ny][nx]:
            stk.append((ny, nx))
            
print(1 if grid[n-1][m-1] == -1 else 0)