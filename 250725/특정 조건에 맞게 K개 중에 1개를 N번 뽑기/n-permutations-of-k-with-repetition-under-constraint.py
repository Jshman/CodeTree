K, N = map(int, input().split())

# Please write your code here.
def sol(array=[], limit_num=K, limit_length=N):
    if len(array) == limit_length:
        if len(set(array)) != 1 or len(array) == 1:
            print(*array)
        return
    
    for i in range(1, K+1):
        array.append(i)
        sol(array, limit_num, limit_length)
        array.pop()
    return

sol()
    
