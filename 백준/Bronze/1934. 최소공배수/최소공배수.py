import sys
input=sys.stdin.readline
temp=0
# 최대공약수 구하기
def gcf(a, b):
  while b != 0:
    temp = a
    a = b
    b = temp % b
  return a

for i in range(int(input())):
  a, b = map(int, input().split())
  print(a*b // gcf(a, b)) # 최소공배수 구하기
