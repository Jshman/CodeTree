n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.

# 좋은 문법이 아닌 것 같음.
def sol(array, s, e):
    tmp = []
    for i in range(len(array)):
        if s <= i+1 and i < e:
            continue
        tmp.append(array[i])
    return tmp


blocks = sol(blocks, s1, e1)
blocks = sol(blocks, s2, e2)

print(len(blocks),*blocks, sep='\n')