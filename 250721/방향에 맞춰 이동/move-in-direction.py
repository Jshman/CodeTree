n = int(input())
moves = [tuple(input().split()) for _ in range(n)]

# Please write your code here.
x, y = 0, 0
dirc = {'N':[0, 1], 'S':[0, -1], 'E':[1, 0], 'W':[-1, 0]}
for move in moves:
    info = dirc[move[0]]
    x += info[0] * int(move[1])
    y += info[1] * int(move[1])
print(x, y)