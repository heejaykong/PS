# 중복 조합 고르는 문제
# 중복O(visited 불필요), 길이제한O(leng, leng_limit 파라미터 필요), 조합(start_num 파라미터 필요)
n, leng_limit = tuple(map(int, input().split()))

def print_arr(arr):
    for el in arr:
        print(el, end=" ")
    print()

def choose(arr, start_num, idx, leng, n, leng_limit):
    if leng == leng_limit:
        print_arr(arr)
        return
    if idx >= n:
        return
    
    for i in range(start_num, n+1):
        arr.append(i)
        
        start_num = i
        choose(arr, start_num, idx + 1, leng + 1, n, leng_limit)
        
        arr.pop()
        
def solution():
    global n, leng_limit
    choose([], 1, 0, 0, n, leng_limit)

solution()