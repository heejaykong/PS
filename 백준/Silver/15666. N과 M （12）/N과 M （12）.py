# 주어진 중복되는 원소(prev 필요)로 조합 만들기 문제
# 중복허용(visited 불필요), 길이제한(leng, leng_limit 필요), 조합(start_idx 필요)
# 이 문제 주의: 주어지는 원소 중 중복되는 원소가 있을 수 있으나, print되는 순열 중 중복되는 게 있으면 안 된다.
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
    
    prev = -1
    for i in range(start_idx, n):
        if basket[i] == prev:
            continue
        
        arr.append(basket[i])
        prev = basket[i]

        start_idx = i
        choose(arr, start_idx, idx + 1, leng + 1, n, leng_limit, basket)

        arr.pop()
        

def solution(n, leng_limit, basket):
    start_idx = 0
    choose([], start_idx, 0, 0, n, leng_limit, basket)

solution(n, leng_limit, basket)