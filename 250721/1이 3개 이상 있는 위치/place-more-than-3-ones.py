n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
ans = 0
for i in range(n):
    for j in range(n):
        now = grid[i][j]
        cnt = 0
        for dy, dx in zip(dys, dxs):
            ny, nx = i + dy, j + dx
            if 0<=ny and ny<n and 0<=nx and nx<n and grid[ny][nx]:
                cnt += 1
        if cnt >= 3: ans += 1

