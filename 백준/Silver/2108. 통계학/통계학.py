import sys
input=sys.stdin.readline
T=int(input())
stack=[]
for i in range(T):
  stack.append(int(input()))
stack.sort()
#1
print(round(sum(stack)/T))
#2
print(stack[len(stack)//2])
#3
from collections import Counter
c = Counter(stack).most_common()
m=[]
if len(c)>1:
  for i in c:
    if i[1] == c[0][1]: m.append(i[0])
  if len(m)>1: print(m[1])
  else: print(m[0])
else: print(c[0][0])
#4
print(max(stack)-min(stack))
