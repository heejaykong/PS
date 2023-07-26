T = int(input())
stack=[]
for i in range(T):
  xy = list(map(int,input().split()))
  stack.append(xy)
stack.sort()
for list in stack:
  print(list[0], list[1])
