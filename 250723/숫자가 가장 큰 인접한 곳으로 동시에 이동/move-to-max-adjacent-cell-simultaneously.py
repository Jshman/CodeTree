dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(y, x, n):
    return 0<=y and y<n and 0<=x and x<n


def sol(grid, marbles):
    leng = len(grid)
    tmp = [[0] * leng for _ in range(leng)]

    for i, j in marbles:
        tmp[i][j] += 1
        M, y, x = -1, -1, -1

        for d in range(4):
            ny, nx = i+dy[d], j+dx[d]
            if not in_range(ny, nx, leng):
                continue
            if grid[i][j] < grid[ny][nx] and M < grid[ny][nx]:
                M, y, x = grid[ny][nx], ny, nx
        if M > -1:
            tmp[y][x] += 1
            tmp[i][j] -= 1

    ret_marbles = []
    for i in range(leng):
        for j in range(leng):
            if tmp[i][j] > 1:
                tmp[i][j] = 0
            elif tmp[i][j] == 1:
                ret_marbles.append((i, j))
    return ret_marbles


if __name__ == '__main__':
    n, m, t = map(int, input().split())

    # Create n x n grid
    a = [list(map(int, input().split())) for _ in range(n)]

    # Get m marble positions
    marbles = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        marbles[i][0] -= 1
        marbles[i][1] -= 1

    for _ in range(t):
        marbles = sol(a, marbles)
    print(len(marbles))
        