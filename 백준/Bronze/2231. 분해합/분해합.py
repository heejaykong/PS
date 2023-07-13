import sys
input=sys.stdin.readline

n = int(input())
for i in range(1, n+1):
  A = list(map(int, str(i)))
  if sum(A)+i == n:
    print(i)
    break
  elif i == n: print(0)
