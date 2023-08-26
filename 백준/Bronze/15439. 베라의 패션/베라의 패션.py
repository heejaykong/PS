import sys
input = sys.stdin.readline
n = int(input())
nums = [i for i in range(n)]
arr = []
ans = 0

def choose(curr_leng):
    global ans

    if curr_leng == 2:
        # print(arr)
        ans += 1
        return

    for i in range(n):
        if curr_leng > 0 and nums[i] == arr[-1]:
            continue
        arr.append(nums[i])
        choose(curr_leng + 1)
        arr.pop()


choose(0)
print(ans)
