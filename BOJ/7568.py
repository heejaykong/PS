# 너무 어렵게 생각해서 복잡하게 푸느라 틀렸음. 결국엔 나보다 키크고 무거운 애들이 몇명 있는지 확인만 하면 되는 문제였다.
# 그래서 혼자 맞게 푼 버전
import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
  stack.append(list(map(int, input().split())))
for i in range(n):
  count = 0
  for j in range(n):
    if i == j: continue
    else:
      if stack[i][0] < stack[j][0] and stack[i][1] < stack[j][1]:
        count += 1
  stack[i].append(count + 1)
for i in stack:
  print(i[-1], end=' ')

# 다른 답안 참고해서 좀 더 개선한 버전
import sys
input=sys.stdin.readline
n=int(input())
stack=[]
for i in range(n):
  stack.append(list(map(int, input().split())))
for i in range(n):
  count = 0
  for j in range(n):
    if i == j: continue
    else:
      if stack[i][0] < stack[j][0] and stack[i][1] < stack[j][1]:
        count += 1
  print(count+1, end=' ') # 굳이 기존의 스택에 추가할 필요 없이 걍 바로 찍어내면 됐었다.
