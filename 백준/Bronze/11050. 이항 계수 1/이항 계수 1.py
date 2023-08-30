n, k = tuple(map(int, input().split()))
nums = [i for i in range(1, n + 1)]
arr = []
ans = 0


def choose(curr_idx, leng):
    global ans
    if leng == k:
        ans += 1
        return

    if curr_idx == n:
        return

    arr.append(nums[curr_idx])
    choose(curr_idx + 1, leng + 1)
    arr.pop()

    choose(curr_idx + 1, leng)


choose(0,0)
print(ans)