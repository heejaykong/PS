# 내 힘으로 푼 버전
import sys
T = int(sys.stdin.readline())
for i in range(T):
  count = 0
  n, m = map(int, sys.stdin.readline().split())
  rank = list(map(int, sys.stdin.readline().split()))
  while rank:
    if rank[0] == max(rank):
      count += 1
      if m == 0: break
      rank.pop(0)
      if m: m -= 1
      else: m = len(rank)-1
    else:
      rank = rank[1:]+rank[:1]
      if m: m -= 1
      else: m = len(rank)-1
  print(count)
