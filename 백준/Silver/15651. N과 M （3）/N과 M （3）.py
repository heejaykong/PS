# 중복O(visited 불필요), 길이제한O(leng, leng_limit 필요), 순서상관O(즉 순열)
n, leng_limit = tuple(map(int, input().split()))

def print_arr(arr):
    for el in arr:
        print(el, end=" ")
    print()

def choose(arr, idx, leng, n, leng_limit):
    if leng == leng_limit:
        print_arr(arr)
        return
    if idx >= n:
        return
    
    for i in range(1, n+1):
        arr.append(i)
        choose(arr, idx + 1, leng + 1, n, leng_limit)
        arr.pop()

def solution():
    global n, leng_limit
    choose([], 0, 0, n, leng_limit)

solution()