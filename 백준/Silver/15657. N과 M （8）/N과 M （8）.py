# 주어진 원소로 중복조합 만드는 문제
# 중복허용(visited 불필요), 길이제한(leng, leng_limit 필요), 조합(start_idx 필요)
n, leng_limit = tuple(map(int, input().split()))
basket = sorted(list(map(int, input().split())))

def print_arr(arr):
    for el in arr:
        print(el, end=" ")
    print()

def choose(arr, start_idx, idx, leng, n, leng_limit, basket):
    if leng == leng_limit:
        print_arr(arr)
        return
    if idx >= n:
        return
    
    for i in range(start_idx, n):
        arr.append(basket[i])
        
        start_idx = i
        choose(arr, start_idx, idx + 1, leng + 1, n, leng_limit, basket)
        
        arr.pop()

def solution(n, leng_limit, basket):
    start_idx = 0
    choose([], start_idx, 0, 0, n, leng_limit, basket)

solution(n, leng_limit, basket)