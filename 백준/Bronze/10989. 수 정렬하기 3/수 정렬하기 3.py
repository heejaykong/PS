import sys
I=sys.stdin.readline
stack=[0]*10001
for i in range(int(I())):
  stack[int(I())] += 1
for i in range(len(stack)):
  if stack[i]:
    for j in range(stack[i]):
      print(i)
