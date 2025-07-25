K, N = map(int, input().split())

def is_same(array):
    pivot = array[0]
    for i in range(1, len(array)):
        if pivot != array[i]:
            return False
    return True

# 연속하여 같은 숫자가 3번 이상 X
def sol(array=[], limit_num=K, limit_length=N):
    if len(array) == limit_length:
        print(*array)
        return
    
    for i in range(1, limit_num+1):
        array.append(i)
        # 연속성 검사
        if not (len(array) >= 3 and is_same(array[-3:])):
            sol(array)
        array.pop()
    return

sol()
    
