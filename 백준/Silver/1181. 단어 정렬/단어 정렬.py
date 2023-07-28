import sys
input = sys.stdin.readline
T = int(input())
stack = set()

for i in range(T):
  stack.add(input().rstrip())

ans = list(stack)
ans.sort(key = lambda x: (len(x), x))
print('\n'.join(ans))
