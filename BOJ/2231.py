# 혼자 못 풀어서 구글링 좀 하고 혼자 풀어본 버전
import sys
input=sys.stdin.readline

n = int(input())
for i in range(1, n+1):
  stack=[]
  for j in range(len(str(i))):
    stack.append((i // 10 ** j) % 10)
  if (sum(stack) + i) == n:
    print(i)
    break
  elif i == n: print(0)

# 다른 답안 참고해서 개선한 버전
import sys
input=sys.stdin.readline

n = int(input())
for i in range(1, n+1):
  A = list(map(int, str(i)))
  if sum(A)+i == n:
    print(i)
    break
  elif i == n: print(0)
