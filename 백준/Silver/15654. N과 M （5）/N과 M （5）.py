# 주어진 원소들로 순열 만들기(중복X(visited 필요), 길이제한O(leng, leng_limit 필요))
n, leng_limit = tuple(map(int, input().split()))
basket = sorted(list(map(int, input().split())))
visited = []

def print_arr(arr):
    for el in arr:
        print(el, end=" ")
    print()

def choose(arr, idx, leng, n, leng_limit, basket):
    if leng == leng_limit:
        print_arr(arr)
        return
    if idx >= n:
        return
    
    for i in range(n):
        if visited[i]:
            continue

        arr.append(basket[i])
        visited[i] = True

        choose(arr, idx + 1, leng + 1, n, leng_limit, basket)
        
        arr.pop()
        visited[i] = False

def solution(n, leng_limit, basket):
    global visited
    visited = [False for i in range(n+1)]
    choose([], 0, 0, n, leng_limit, basket)

solution(n, leng_limit, basket)