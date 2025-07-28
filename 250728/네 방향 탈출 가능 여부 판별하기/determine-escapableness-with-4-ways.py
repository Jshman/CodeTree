from collections import deque

def in_range(y, x, h, w):
    return 0<=y and y<h and 0<=x and x<w

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

dyxs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
q = deque()
q.append((0, 0))
while q:
    y, x = q.popleft()
    a[y][x] = -1
    if y == n-1 and x == m-1:
        break
    for dy, dx in dyxs:
        ny, nx = y+dy, x+dx
        if in_range(ny, nx, n, m) and a[ny][nx]==1:
            q.append((ny, nx))
print(1 if a[n-1][m-1] == -1 else 0)