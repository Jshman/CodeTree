from collections import deque

n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dyxs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
ans = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            visited = [[False]*n for _ in range(n)]

            q = deque()
            q.append((i, j, 0))

            while q:
                y, x, times = q.popleft()
                if grid[y][x] == 3:
                    ans[i][j] = times
                    break
                
                for dy, dx in dyxs:
                    ny, nx = y+dy, x+dx
                    if 0>ny or ny>=n or 0>nx or nx>=n or grid[ny][nx] == 1 or visited[ny][nx]:
                        continue
                    q.append((ny, nx, times+1))
                    visited[ny][nx] = True
            else:
                ans[i][j] = -1

for elem in ans:
    print(*elem)
