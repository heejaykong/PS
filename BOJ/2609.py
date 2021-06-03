# 자꾸 틀려서 결국 구글링으로 찾아본 결과 **유클리드 호제법**을 알아야 제대로 풀 수 있었던 문제
# 그래서 아래와 같이 풀어서 맞췄다
import sys
input=sys.stdin.readline
A, B = map(int, input().split())
a = max(A, B)
b = min(A, B)
# 최대공약수
while b != 0:
  temp = a
  a = b
  b = temp % b
print(a)
# 최소공배수
print(A*B // a)


# 재귀로 풀어본 버전
import sys
input=sys.stdin.readline
A, B = map(int, input().split())
a = max(A, B)
b = min(A, B)
# 최대공약수
def gcd(a, b):
  if b == 0: return a
  else: return gcd(b, a%b)
print(gcd(a,b))
# 최소공배수
print(A*B // gcd(a,b))
