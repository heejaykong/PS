import sys
n, k = map(int, sys.stdin.readline().split())
stack = list(range(1,n+1))
ans = []
i = 0
while stack:
  i = (i+(k-1)) % len(stack)
  ans.append(str(stack.pop(i)))
print(f'<{", ".join(ans)}>')