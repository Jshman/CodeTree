n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

dyxs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
ans = 0
for i, j in points:
    cnt = 0
    stack = [(i-1, j-1)]
    while stack:
        y, x = stack.pop()
        if grid[y][x] != 0:
            continue
        grid[y][x] = -1
        cnt += 1

        for dy, dx in dyxs:
            ny, nx = y+dy, x+dx
            if 0>ny or ny>=n or 0>nx or nx>=n or grid[ny][nx] != 0:
                continue
            stack.append((ny, nx))
    ans += cnt
print(ans)