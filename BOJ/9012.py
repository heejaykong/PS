# 내 힘으로 푼 것
T=int(input())
for i in range(T):
  temp=[]
  stack=list(input())
  for char in stack:
    if char == '(':
      temp.append(char)
    elif temp and temp[-1]=='(':
        temp.pop()
    else:
        temp.append(char)
  if temp: print('NO')
  else: print('YES')

# 다른 답안1(그냥 덧셈뺄셈으로 우습게 풀어버린)
from sys import stdin
n = int(input())
for _ in range(n):
    str_ = stdin.readline().strip()
    stack = 0
    for chr_ in str_:
        if chr_ == '(':
            stack += 1
        else:
            stack -= 1
            if stack < 0:
                break
    if stack == 0:
        print('YES')
    else:
        print('NO')

# 다른 답안2(for-else문을 처음 알게 해준)
import sys
T = int(sys.stdin.readline())
for _ in range(T):
    D = sys.stdin.readline().strip()
    stack = []
    for p in D:
        if p == '(':
            stack.append(p)
        else:
            if len(stack):
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')
