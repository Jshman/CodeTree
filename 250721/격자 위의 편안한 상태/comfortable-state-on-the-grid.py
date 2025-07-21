n, m = map(int, input().split())
grid = [[0]*n for _ in range(n)]

dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

for _ in range(m):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    
    # 페인트칠
    grid[r][c] = 1

    # 4방위 확인
    cnt = 0
    for d in range(4):
        ny, nx = r+dy[d], c+dx[d]
        if 0<=ny and ny<n and 0<=nx and nx<n and grid[ny][nx] == 1:
            cnt += 1
    print(1 if cnt == 3 else 0)