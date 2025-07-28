from collections import deque

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

villages = 0
vill_info = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            villages += 1
            q = deque()
            q.append((i, j))

            people = 0
            while q:
                y, x = q.popleft()
                grid[y][x] = -1
                for dy, dx in zip([0, 1, 0, -1], [1, 0, -1, 0]):
                    ny, nx = y+dy, x+dx
                    if 0>ny or ny>=n or 0>nx or nx>=n or grid[ny][nx] != 1 or visited[ny][nx]:
                        continue
                    q.append((ny, nx))
                    visited[ny][nx] = True
                people += 1
            vill_info.append(people)
vill_info.sort()


print(villages, *vill_info, sep='\n')