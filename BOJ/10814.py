# 혼자 푼 버전
import sys
input=sys.stdin.readline
n=int(input())
mems=[]
for i in range(n):
  mems.append(input().split())
mems.sort(key = lambda x: int(x[0]))
for mem in mems: print(mem[0], mem[1])

# 파이썬의 sort() 함수를 쓰지 않고 정렬하려면 아래와 같이 할 수 있음
# 아예 빈 리스트를 초기화해서 각 index를 나이 삼아 append하고, 순서대로 찍어내는 방법임. 3차원 배열을 쓰는 셈...
import sys
input=sys.stdin.readline
n=int(input())
mems=[[] for _ in range(201)]
for i in range(n):
  mem = input().split()
  mems[int(mem[0])].append(mem)
for mem in mems:
  if len(mem):
    for i in mem:
      print(i[0], i[1])
