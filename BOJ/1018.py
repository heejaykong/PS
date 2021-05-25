# 푸는 데 시간을 좀 많이... 쓴 문제
# 처음 혼자 풀 때 접근법은:
# 새로 칠해줘야 할 블록의 index에 1로 표시하고 나머지는 0으로 표시한 중첩 list를,
# (0,0)번째 블록이 흰색일 때와 검정색일 때, 이렇게 두 가지 경우를 고려해서 각각 만들어 준 뒤,
# 그 두 개의 중첩 list를 8*8 크기만큼 스캔해서, 1의 합이 가장 적게 잡힐 경우를 리턴해줬다

# 혼자 풀때는 8*8 크기만큼 스캔하는 부분이 막혀서 구글링을 좀 했다. 그래서 아래와 같이 풀었음
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
stack=[]
count_w=[[0 for _ in range(m)] for _ in range(n)]
count_b=[[0 for _ in range(m)] for _ in range(n)]

# (0,0)번째 블록이 흰색일 경우 count_w 리스트를 초기화시키는 함수
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

# (0,0)번째 블록이 검정색일 경우 count_b 리스트를 초기화시키는 함수
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
        if count_w[i][j]: w += 1
        if count_b[i][j]: b += 1
    ans = min(ans, min(w, b))
print(ans)


# 다음은 다른 답안들을 보고 개선한 버전이다
# 굳이 0과 1로 이루어진 중첩 list 두 개를 따로 만들 필요는 없었다
