# 혼자 풀어본 버전
# 무조건 2개 건너뛰되, 2개 건너뛰는 자리가 나쁜구름이면 1개 뛰는 걸로 변경해서 끝까지 가는 식
# (IndexError: list index out of range 처리 때문에 코드가 지저분해져서 맘에 안 듦)
def jumpingOnClouds(c):
  i = 0
  cnt = 0
  
  while i != len(c)-1:  # 마지막 원소에 다다를때까지 반복해라
    # 최소 2개 원소는 뒤에 남아있다는 조건하에 2개를 뛰어서 나쁜구름을 밟게 된다면, or 마지막에서 두번째 원소라면
    if (i < len(c)-2 and c[i+2]==1) or (i == len(c)-2):
      i += 1  # 1개 구름만 뛰는 걸로 변경해라
    else:
      i += 2
    cnt += 1
    
  return cnt

# 같은 로직이지만 좀더 가독성 좋은 코드(if-else의 순서가 바뀜으로써 훨씬 명료해짐)
def jumpingOnClouds(c):
  goal_index = len(c)-1  # 아예 마지막 index를 이렇게 변수화
  current = 0
  answer = 0
  
  while(current < goal_index):
    if current + 2 <= goal_index and c[current + 2] == 0:  # 2개 구름을 건너뛰는게 여러모로 안전한 상황이라면
      current += 2  # 2개 구름을 뛰어도 좋다
    else:
      current += 1
    answer += 1
    
  return answer

