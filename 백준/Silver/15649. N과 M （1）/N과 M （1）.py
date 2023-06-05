n, leng_limit = tuple(map(int, input().split()))

def print_arr(arr):
    for el in arr:
        print(el, end=" ")
    print()

visited = []
def choose(arr, idx, leng, n, leng_limit):
    if leng == leng_limit:
        print_arr(arr)
        return
    if idx >= n:
        return
    
    for i in range(1, n+1):
        if visited[i]:
            continue

        arr.append(i)
        visited[i] = True
        
        choose(arr, idx + 1, leng + 1, n, leng_limit)
        
        arr.pop()
        visited[i] = False
        
def solution():
    global visited, n, leng_limit
    visited = [False for i in range(n+1)]
    choose([], 0, 0, n, leng_limit)

solution()