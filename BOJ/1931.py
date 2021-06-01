# 혼자 힘으로 푼 버전
# 회의가 끝나는 시각을 오름차순으로 정렬한 뒤, 가능해지는 스케줄링으로 추려내면 가장 촘촘하게 회의를 배치할 수 있다
# 그러므로 맨 첫번째 회의(가장 빠른 시'각'에 끝내는 회의)의 끝나는 시간보다 같거나 큰 시각에 시작하는 회의가 나오면 선택하고
# 선택한 회의의 끝나는 시각보다 같거나 큰 시각에 시작하는 회의가 나오면 선택하고... 이걸 스택이 끝날 때까지 반복한다
stack = []
for i in range(int(input())):
  stack.append(list(map(int, input().split())))

stack.sort(key=lambda x: (x[1], x[0]))

cnt = 0
finish = -1
for item in stack:
  if item[0] < finish: continue
  else:
    cnt += 1
    finish = item[1]
print(cnt)

