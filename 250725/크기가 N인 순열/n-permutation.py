n = int(input())

# Please write your code here.
def sol(array=[], limit=n):
    if len(array) == limit:
        if len(set(array)) == limit:
            print(*array)
        return
    
    for i in range(1, limit+1):
        if i in set(array):
            continue
        array.append(i)
        sol(array)
        array.pop()
    return
    
sol()