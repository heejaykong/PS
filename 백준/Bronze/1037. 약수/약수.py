import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int, input().split()))
stack.sort()
print(stack[0]*stack[-1])
