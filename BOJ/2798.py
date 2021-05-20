# 검색해서 좀 참고해서 혼자 푼 버전
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for i in range(n-2):
  for j in range(1, n-1):
    for k in range(2, n):
      if i==j or j==k or i==k or cards[i] + cards[j] + cards[k] > m:
        continue
      else:
        ans = max(ans, cards[i] + cards[j] + cards[k])
print(ans)

# 더 개선한 버전
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
ans = 0
for i in range(n-2):
  for j in range(i+1, n-1): # i+1에서 시작하면 됨
    for k in range(j+1, n): # 얘도 마찬가지로 j+1에서 시작하면 중복되는 구성없이 루프 가능
      if cards[i] + cards[j] + cards[k] > m:
        continue
      else:
        ans = max(ans, cards[i] + cards[j] + cards[k])
print(ans)
