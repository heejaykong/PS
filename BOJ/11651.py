# 처음에 인풋 받을 때 sys로 안하고 그냥 input으로 했더니 시간초과 뜸
# 그래서 아래와 같이 씀
import sys
input = sys.stdin.readline
T=int(input())
stack=[]
for i in range(T):
  stack.append(list(map(int, input().split())))
stack.sort(key = lambda x: (x[1], x[0]))
for i in stack:
  print(i[0], i[1])
