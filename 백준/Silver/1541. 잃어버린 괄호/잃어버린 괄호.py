stack = input().split('-')
for i in range(len(stack)):
  num = sum(list(map(int, stack[i].split('+'))))
  stack[i] = num
ans = stack[0]
for i in range(1, len(stack)):
  ans -= stack[i]
print(ans)
