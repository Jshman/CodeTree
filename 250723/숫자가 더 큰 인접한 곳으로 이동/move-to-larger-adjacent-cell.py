def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n

n, r, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
r, c = r-1, c-1

now = a[r][c]
trace = [now]

dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
while 1:
    # 주변에 자신보다 큰 수가 있는지 탐색
    for d in range(4):
        ny, nx = r+dy[d], c+dx[d]
        if in_range(ny, nx) and a[ny][nx] > now:
            r, c = ny, nx
            now = a[r][c]
            trace.append(now)
            break
    else:
        print(*trace)
        break