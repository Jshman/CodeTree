def rotate(grid, r1, r2, c1, c2):
    right_up = grid[r1][c2]

    # 위
    for i in range(c2, c1, -1):
        grid[r1][i] = grid[r1][i-1]
    # 왼쪽 변
    for i in range(r1, r2):
        grid[i][c1] = grid[i+1][c1]
    # 아랫 변 
    for i in range(c1, c2):
        grid[r2][i] = grid[r2][i+1]
    # 오른쪽 변
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i-1][c2]
    
    # 이동 중 사라진 자리에 추가
    grid[r1+1][c2] = right_up

    return grid

def in_range(y, x, h, w):
    return 0<=y and y<h and 0<=x and x<w

dy, dx = [0, -1, 0, 1], [1, 0, -1, 0]

def change(grid, r1, r2, c1, c2):
    tmp = [[grid[i][j] for j in range(len(grid[0]))] for i in range(len(grid))]

    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            now = grid[i][j]
            cnt = 1
            for d in range(4):
                ny, nx = i+dy[d], j+dx[d]
                if not in_range(ny, nx, len(grid), len(grid[0])):
                    continue
                cnt += 1
                now += grid[ny][nx]
            tmp[i][j] = now // cnt

    return tmp


n, m, Q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1

    grid = rotate(grid, r1, r2, c1, c2)
    grid = change(grid, r1, r2, c1, c2)
for elem in grid:
    print(*elem)