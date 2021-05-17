# 2750와 똑같지만 좀 다르게
import sys
I=sys.stdin.readline
stack=[]
for i in range(int(I())):
    stack.append(int(I()))
stack.sort()
print('\n'.join(map(str, stack)))
