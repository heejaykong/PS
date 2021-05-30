# 혼자 힘으로 푼 버전
n, k = map(int, input().split())
stack = []
for i in range(n):
  stack.append(int(input()))
ans = 0
for i in range(n-1, -1, -1):
  if k // stack[i] > 0:
    ans += k // stack[i]
    k %= stack[i]
print(ans)
