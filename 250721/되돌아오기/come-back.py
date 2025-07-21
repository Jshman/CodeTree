dy, dx = [1, 0, -1, 0], [0, 1, 0, -1]
s = {'N':0, 'E':1, 'S':2, 'W':3}

N = int(input())

y, x = 0, 0
times = 0
for _ in range(N):
    d, m = input().split()
    m = int(m)
    d = s[d]
    
    for i in range(m):
        y += dy[d]
        x += dx[d]
        times += 1
        if y == 0 and x == 0:
            break
    else:
        continue
    break
print(times)