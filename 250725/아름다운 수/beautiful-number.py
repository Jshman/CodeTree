N = int(input())
cnt = 0

def is_beautiful(array):
    idx = 0
    while idx < len(array):
        pivot = array[idx]
        cnt = 0
        for i in range(idx, min(len(array), idx+pivot)):
            if pivot != array[i]:
                return False
            cnt += 1
        idx += pivot    
        if cnt != pivot:
            return False
    return True


def sol(array=[], limit=N):
    global cnt

    if len(array) == limit:
        if is_beautiful(array):
            cnt += 1
        return

    for i in range(1, 4+1):
        array.append(i)
        sol(array, limit)
        array.pop()
    return

sol()
print(cnt)