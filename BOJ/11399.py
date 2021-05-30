# 혼자 힘으로 푼 버전
n=int(input())
stack = list(map(int, input().split()))
stack.sort()
ans = 0
for i in range(n):
  count = 0
  for j in range(n):
    if j <= i:
      count += stack[j]
    else: continue
  ans += count
print(ans)

# 다른 답안 보고 개선한 버전
n=int(input())
stack = list(map(int, input().split()))
stack.sort()
ans = 0
cur = 0
for time in stack: # 굳이 이중 루프 돌 필요 없이, 두 개 변수로 누적합산하면 된다
  cur += time
  ans += cur
print(ans)
