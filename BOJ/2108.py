# 쌩으로 혼자 풀진 않았지만(약간의 구글링 참고 및 제출해보고 틀려서 디버깅) 우선 내가 낸 버전

# 계속 '틀렸습니다'가 뜨길래 당연히 3번째 최빈값 구하는 데서 틀린 줄 알고 애먼 데서 시간 낭비하다가
# 1번의 산술평균을 출력하는 부분에서 계속 틀려왔다는 충격적인 사실을 알아냄
# 소수점 이하 첫째 자리에서 반올림한 값을 출력해야 됐는데, round(sum(stack)//T)으로 썼다가, round(sum(stack)/T)으로 바꿔서 맞출 수 있었다.
# 결론적으로 python에서 '//'연산과 '/'연산의 차이를 다시는 무시하지 말자...
import sys
input=sys.stdin.readline
T=int(input())
stack=[]
for i in range(T):
  stack.append(int(input()))
stack.sort()
# 1번 산술평균
print(round(sum(stack)/T))
# 2번 중앙값
print(stack[len(stack)//2])
# 3번 최빈값, 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
from collections import Counter
c = Counter(stack).most_common()
m=[]
if len(c)>1:
  for i in c:
    if i[1] == c[0][1]: m.append(i[0])
  if len(m)>1: print(m[1])
  else: print(m[0])
else: print(c[0][0])
# 4번 범위
print(max(stack)-min(stack))
