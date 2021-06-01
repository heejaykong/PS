# 혼자 못 풀어서 구글링 좀 참고해서 풀어본 버전
stack = input().split('-')
for i in range(len(stack)):
  if '+' in stack[i]:
    num = sum(list(map(int, stack[i].split('+'))))
    stack[i] = num
ans = int(stack[0])
for i in range(1, len(stack)):
  ans -= int(stack[i])
print(ans)

# 생각해보니 if문 굳이 필요 없었다. 그래서 바꾼 버전
stack = input().split('-')
for i in range(len(stack)):
  num = sum(list(map(int, stack[i].split('+'))))
  stack[i] = num
ans = stack[0] # 그러면 스택 안의 모든 식을 다 돌기 때문에 굳이 int로 다 감싸지 않아도 된다
for i in range(1, len(stack)):
  ans -= stack[i]
print(ans)
