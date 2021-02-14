# https://blog.naver.com/ndb796/221234427842
import sys
T = int(sys.stdin.readline())
matrix = []
for row in range(T):
  matrix.append(list(map(int, sys.stdin.readline().split())))

for k in range(T):
  for i in range(T):
    for j in range(T):
      if matrix[i][k] and matrix[k][j]:
        matrix[i][j] = 1

for i in range(T):
  for j in range(T):
    print(matrix[i][j], end=" ")
  print()
