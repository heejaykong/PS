import sys
input = sys.stdin.readline
T=int(input())
stack=[]
for i in range(T):
  stack.append(list(map(int, input().split())))
stack.sort(key = lambda x: (x[1], x[0]))
for i in stack:
  print(i[0], i[1])
