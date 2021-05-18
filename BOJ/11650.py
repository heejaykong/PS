T = int(input())
stack=[]
for i in range(T):
  xy = list(map(int,input().split()))
  stack.append(xy)
stack.sort() # 더 정확히 하고 싶다면 아래와 같이 하면 됨
# stack.sort(key = lambda x: (x[0], x[1])) # 0번째 인자 우선 정렬, 그 다음 1번째 인자 정렬한다는 의미
for list in stack:
  print(list[0], list[1])
