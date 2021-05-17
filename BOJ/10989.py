# 처음에 메모리 초과 나서 질문게시판 보고 혼자 풀어본 버전
import sys
I=sys.stdin.readline
stack=[0]*10001
for i in range(int(I())):
  stack[int(I())] += 1
for i in range(len(stack)):
  if stack[i]:
    for j in range(stack[i]):
      print(i)

# 다른 사람꺼 참고한 버전
import sys
I=sys.stdin.readline
stack=[0]*10001
for i in range(int(I())):
  stack[int(I())] += 1
for i in range(len(stack)):
  if stack[i]:
    print(f'{i}\n' * stack[i], end='') # 찍어내는 부분에서 루프를 안 쓰고 이렇게 처리하니까 시간이 거의 절반 줄어듦
