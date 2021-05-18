# 혼자서 푼 버전
import sys
input = sys.stdin.readline
T = int(input())
stack = []

for i in range(T):
    word = input().strip()
    if word in stack: continue
    else: stack.append(word)
stack.sort(key = lambda x: (len(x), x))

print('\n'.join(stack))


# 다른 답안 참고해서 개선한 버전(set을 활용해서 중복처리 부분을 더 간소화했다. 속도가 훨씬 빨라짐)
import sys
input = sys.stdin.readline
T = int(input())
stack = set()

for i in range(T):
  stack.add(input().rstrip()) # set(=집합)이기 때문에 중복된 아이템이 들어오면 걍 스루한다

ans = list(stack)
ans.sort(key = lambda x: (len(x), x))

print('\n'.join(ans))
