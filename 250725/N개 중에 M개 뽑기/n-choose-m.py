N, M = map(int, input().split())

# Please write your code here.
def sol(now=1, array=[], limit_length=M, limit_num=N):
    if len(array) == limit_length:
        print(*array)

    for i in range(now, limit_num+1):
        array.append(i)
        sol(i+1, array)
        array.pop()

sol()