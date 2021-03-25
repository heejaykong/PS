# 2557
print('Hello World!')

# 1000
a, b = map(int, input().split())
print(a+b)

# 2558
a=int(input())
b=int(input())
print(a+b)

# 10950
T=int(input())
for i in range(T):
  a, b = map(int, input().split())
  print(a+b)

# 10951
import sys
while True:
  try:
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
  except:
    break

# 10952
import sys
while True:
  try:
    a, b = map(int, sys.stdin.readline().split())
    if (a==0 and b==0):
      break
    else:
      print(a+b)
  except:
    break

# 10953
T = int(input())
for i in range(T):
  a,b=map(int,input().split(','))
  print(a+b)

# 11021
T=int(input())
for i in range(1,T+1):
  a,b=map(int,input().split())
  print(f'Case #{i}: {a+b}')

# 11022
import sys
T=int(sys.stdin.readline())
for i in range(T):
  a,b=map(int, sys.stdin.readline().split())
  print(f'Case #{i+1}: {a} + {b} = {a+b}')

# 11718
while True:
  try:
    print(input())
  except:
    break
# 또는
import sys
for line in sys.stdin:
    print(line, end='')

# 11719(11718과 거의 유사)
while True:
  try:
    print(input())
  except:
    break

# 11720
N=int(input())
nums=list(map(int, list(input())))
sum=0
for i in range(N):
  sum += nums[i]
print(sum)
# 또는
input()
print(sum(map(int,input())))

# 11721
str = input()
i=0
while len(str) > i:
  print(str[i:i+10])
  i+=10
# 또는
str=input()
for i in range(0, len(str), 10):
  print(str[i:i+10])
