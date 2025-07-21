def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<n

if __name__=='__main__':
    n = int(input())
    grid = [[0] * n for _ in range(n)]

    y, x = n-1, n-1
    number = n**2

    # 서 북 동 남
    dy, dx = [0, -1, 0, 1], [-1, 0, 1, 0]
    dirc = 0

    while 1:
        grid[y][x] = number
        if number == 1:
            break
        
        ny, nx = y+dy[dirc], x+dx[dirc]
        if not in_range(ny, nx) or grid[ny][nx] > 0:
            dirc = (dirc+1)%4
            continue
        
        number -= 1
        y, x = ny, nx

    for elem in grid:
        print(*elem)
    