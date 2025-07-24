n, m, r, c = map(int, input().split())

# Please write your code here.
boom = set()
boom.add((r-1, c-1))

dxys = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def in_range(y, x, n):
    return 0<=y and y<n and 0<=x and x<n

def simul(boom, time, leng):
    dist = 2**(time-1)
    n = len(boom)
    boom_list = list(boom)
    for i in range(n):
        y, x = boom_list[i]

        for dy, dx in dxys:
            ny, nx = y+(dy*dist), x+(dx*dist)
            if not in_range(ny, nx, leng):
                continue
            boom.add((ny, nx))
    return boom

for t in range(m):
    boom = simul(boom, t+1, n)
print(len(boom))