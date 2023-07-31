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
