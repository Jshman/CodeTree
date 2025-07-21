dirs = input()

# 북동남서
dy, dx = [-1, 0, 1, 0], [0, 1, 0, -1]

x, y = 0, 0
dir_num = 0

for c in dirs:
    if c == 'F':
        if dir_num == 0:
            y += 1
        elif dir_num == 1:
            x += 1
        elif dir_num == 2:
            y -= 1
        elif dir_num == 3:
            x -= 1
    elif c == 'L':
        dir_num = (dir_num-1)%4
    elif c == 'R':
        dir_num = (dir_num+1)%4

print(x, y)