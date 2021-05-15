# 스스로 푼 버전
def count_digit(num): # 몇자리 수인지 구하는 함수
  ans = 1
  while True:
    if num < 10: break
    num //= 10
    ans += 1
  return ans

stack=[]
for j in range(1, 10001):
  num = 0
  digit_sum = 0
  # !(셀프넘버) 구하기
  for i in range(count_digit(j)):
    digit = j // 10**i % 10
    digit_sum += digit
  num = j + digit_sum
  stack.append(num)

# 범위 내 셀프넘버만 찍기
for i in range(1, 10001):
  if i in stack:
    continue
  else: print(i)

    
# 다른 사람들 답안 참고해서 개선해본 버전. 시간이 훨씬 덜 걸림(10000짜리 stack을 전부 0으로 초기화하고 index를 이용함)
def count_digit(num): # 몇자리 수인지 구하는 함수
  ans = 1
  while True:
    if num < 10: break
    num //= 10
    ans += 1
  return ans

stack=[0]*10001
for j in range(1, 10001):
  num = 0
  digit_sum = 0
  # !(셀프넘버) 구하기
  for i in range(count_digit(j)):
    digit = j // 10**i % 10
    digit_sum += digit
  num = j + digit_sum
  try:
    stack[num] = 1
  except IndexError: # 새로 배웠다... try-except문에서 IndexError 사용하기
    continue
# 범위 내 셀프넘버만 찍기
for i in range(1, 10001):
  if stack[i]: # 해당 index가 표시되어 있지 않다면 그 숫자 찍어내기
    continue
  else: print(i)
