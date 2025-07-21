def in_range(y, x):
    return 0<=y and y<n and 0<=x and x<m

if __name__=='__main__':
    n, m = map(int, input().split())
    arr = [[0] * m for _ in range(n)]

    y, x = 0, 0
    dys, dxs = [-1, 0, 1, 0], [0, 1, 0, -1]
    dirc = 0
    num = 1

    while 1:
        arr[y][x] = num
        if num == n*m : break

        ny, nx = y+dys[dirc], x+dxs[dirc]
        if not in_range(ny, nx) or arr[ny][nx] > 0:
            dirc = (dirc+1)%4
            continue
        num += 1
        y, x = ny, nx

    for elem in arr:
        print(*elem)
