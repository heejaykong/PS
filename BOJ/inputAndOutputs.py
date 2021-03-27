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

# 2741
N = int(input())
for i in range(1, N+1):
  print(i)

# 2742
N = int(input())
for i in range(N, 0, -1):
  print(i)

# 2739
N = int(input())
for i in range(1, 10):
  print(f'{N} * {i} = {N*i}')

# 1924
import sys
x, y = map(int, sys.stdin.readline().split())
name = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
temp = 0
for i in range(0, x-1):
  temp += days[i]
temp += y
print(name[temp % 7])
# 또는
x, y = map(int, input().split())
for i in range(1, x):
    if i in [1, 3, 5, 7, 8, 10, 12]: # list로 in문법을 쓸 수 있음
        y += 31 #따로 temp라는 변수 없이 입력받은 일수(y)를 바로 쓸 수 있음
    elif i == 2:
        y += 28
    else:
        y += 30
day_week = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(day_week[y % 7])

# 8393
n=int(input())
for i in range(n-1, 0, -1):
  n += i
print(n)
# 아래가 더 좋은 답
n=int(input())
print(n*(n+1) // 2)

# 10818
import sys
n=int(sys.stdin.readline())
nums=list(map(int, sys.stdin.readline().split()))
print(min(nums), max(nums))

# 2438
N=int(input())
for i in range(1, N+1):
  print('*' * i)

# 2439
N=int(input())
for i in range(1, N+1):
  print(('*' * i).rjust(N))
  # 또는
  # print(' ' * (N-i) + '*' * i) # 이게 더 빠른듯

# 2440
N=int(input())
for i in range(N, 0, -1):
  print('*' * i)

# 2441
N=int(input())
for i in range(N):
  print(' ' * i + '*' * (N-i))

# 2442
N=int(input())
for i in range(1, N+1):
  print(' ' * (N-i) + '*' * (2*i-1))

# 2445
N=int(input())
for i in range(N-1, -N, -1):
  temp = abs(i)
  print('*' * (N-temp) + ' ' * (2*temp) + '*' * (N-temp))

# 2522
N=int(input())
for i in range(-N+1, N):
  temp=abs(i)
  print(' ' * temp + '*' * (N-temp))

# 2446
N=int(input())
for i in range(N-1, -N, -1):
  temp=abs(i)
  print(' ' * (N-temp-1) + '*' * (2*temp+1))

# 10991
N=int(input())
for i in range(1, N+1):
  print(' ' * (N-i) + '* ' * i)

# 10992
N=int(input())
for i in range(1, N+1):
  if i==1 or i==N:
    print(' ' * (N-i) + '*' * (2*i-1))
  else:
    print(' ' * (N-i) + '*' + ' ' * (2*i-3) + '*')
