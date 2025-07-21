n, t = map(int, input().split())
r, c, d = input().split()
y, x = int(r), int(c)

# Please write your code here.
dirc = {'U':'D', 'R':'L', 'D':'U', 'L':'R'}

for _ in range(t):
    if d == 'U':
        if y == n:
            d = dirc[d]
            continue
        y += 1
    elif d == 'R':
        if x == n:
            d = dirc[d]
            continue
        x += 1
    elif d == 'D':
        if y == 1:
            d = dirc[d]
            continue
        y -= 1
    elif d == 'L':
        if x == 1:
            d = dirc[d]
            continue
        x -= 1
print(y, x)