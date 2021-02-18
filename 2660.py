import sys
import math
matrix = []
pplCount = int(sys.stdin.readline())

# init
for i in range(pplCount):
    matrix.append([math.inf for i in range(pplCount)])
for i in range(pplCount):
    matrix[i][i] = 0

while True:
    input = sys.stdin.readline().split()
    if "-1" in input:
        break
    a, b = map(int, input)
    matrix[a-1][b-1] = 1
    matrix[b-1][a-1] = 1

# 점수 매기기
for k in range(pplCount):
    for i in range(pplCount):
        for j in range(pplCount):
            if i!=j and i!=k and k!=j:
                if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                    matrix[i][j] = matrix[i][k] + matrix[k][j]

# 회장 후보 선출
candidateList = []
scores = []
for i in range(pplCount):
    scores.append(max(matrix[i]))
for i in range(pplCount):
    if max(matrix[i]) == min(scores):
        candidateList.append(i+1)

print(min(scores), scores.count(min(scores)))
print(' '.join(list(map(str, sorted(candidateList)))))
