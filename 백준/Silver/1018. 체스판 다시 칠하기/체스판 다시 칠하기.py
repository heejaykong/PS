import sys
input=sys.stdin.readline
n,m=map(int,input().split())
stack=[]
count_w=[[0 for _ in range(m)] for _ in range(n)]
count_b=[[0 for _ in range(m)] for _ in range(n)]

def paint_w_first(stack):
  for i in range(len(stack)):
    for j in range(len(stack[i])):
      if i % 2 == 0:
        if j % 2 == 0:
          if stack[i][j] == 'W': continue
          else: count_w[i][j] = 1
        else:
          if stack[i][j] == 'W': count_w[i][j] = 1
          else: continue
      else:
        if j % 2 == 1:
          if stack[i][j] == 'W': continue
          else: count_w[i][j] = 1
        else:
          if stack[i][j] == 'W': count_w[i][j] = 1
          else: continue
  # print(count_w)

def paint_b_first(stack):
  for i in range(len(stack)):
    for j in range(len(stack[i])):
      if i % 2 == 0:
        if j % 2 == 0:
          if stack[i][j] == 'B': continue
          else: count_b[i][j] = 1
        else:
          if stack[i][j] == 'B': count_b[i][j] = 1
          else: continue
      else:
        if j % 2 == 1:
          if stack[i][j] == 'B': continue
          else: count_b[i][j] = 1
        else:
          if stack[i][j] == 'B': count_b[i][j] = 1
          else: continue
  # print(count_b)

for i in range(n):
  stack.append(list(input().rstrip()))
paint_w_first(stack)
paint_b_first(stack)

ans = 50*50
for start_n in range(n-7):
  for start_m in range(m-7):
    w = 0
    b = 0
    for i in range(start_n, start_n + 8):
      for j in range(start_m, start_m + 8):
    #     print(count_w[i][j], end='')
    #   print()
    # print()
        if count_w[i][j]: w += 1
        if count_b[i][j]: b += 1
    ans = min(ans, min(w, b))
print(ans)
