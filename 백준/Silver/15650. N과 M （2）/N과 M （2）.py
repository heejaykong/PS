# 중복X(visited 배열 필요), 길이제한O(leng 파라미터 필요), 조합이어야 함(start_num 파라미터 필요)
n, leng_limit = tuple(map(int, input().split()))

visited = []

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
        if visited[i]:
            continue

        arr.append(i)
        visited[i] = True
        
        start_num = i
        choose(arr, start_num, idx + 1, leng + 1, n, leng_limit)

        arr.pop()
        visited[i] = False

def solution():
    global visited, n, leng_limit
    visited = [False for i in range(n+1)]
    choose([], 1, 0, 0, n, leng_limit)

solution()