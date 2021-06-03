# 혼자 힘으로 푼 버전. 딱히 더 개선할 필요 없음
import sys
input=sys.stdin.readline
n=int(input())
stack=list(map(int, input().split()))
stack.sort()
print(stack[0]*stack[-1])
