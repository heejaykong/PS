from collections import deque
import sys
n=int(sys.stdin.readline())
cards=deque(range(1,n+1))
if n > 1: cards.popleft()
while len(cards) > 1:
  cards.append(cards.popleft())
  cards.popleft()
print(cards[0])