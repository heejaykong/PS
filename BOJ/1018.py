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
import sys
input=sys.stdin.readline
n,m=map(int, input().split())
stack=[]

for i in range(n):
  stack.append(input().rstrip()) # 참고로, 체스판을 꼭 list로 초기화하지 않고 string으로만 append해도 루프에서 잘만 돌더라.

ans = []
# 루프 안에서 돌면서 8*8 크기로 잘랐을 때 바꿔 칠해야 할 블록 갯수를 매번 세고,
# 그걸 매번 ans 스택에 append해준 다음에 최소값을 찍어내는 식으로 하면 코드가 더 간단해진다
# 근데 다시 보니 위 코드보다 더 효율적이게 되는 거 같진 않아 보인다...
for start_n in range(n-7):
  for start_m in range(m-7):
    w = 0 # 흰색으로 시작한다 가정할때 바꿔 칠해야 할 블록 갯수
    b = 0 # 검정색으로 시작한다 가정할때 바꿔 칠해야 할 블록 갯수
    for i in range(start_n, start_n + 8):
      for j in range(start_m, start_m + 8):
        if (i+j) % 2 == 0: # 그냥 index 두개를 더해서 홀수인지 짝수인지 봐도 it works!!!
          if stack[i][j] != 'W': w += 1
          if stack[i][j] != 'B': b += 1
        else:
          if stack[i][j] != 'B': w += 1
          if stack[i][j] != 'W': b += 1
    ans.append(w)
    ans.append(b)
print(min(ans))
