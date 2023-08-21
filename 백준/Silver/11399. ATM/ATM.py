n=int(input())
stack = list(map(int, input().split()))
stack.sort()
ans = 0
cur = 0
for time in stack:
  cur += time
  ans += cur
print(ans)
