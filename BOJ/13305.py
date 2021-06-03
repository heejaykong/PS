# 처음에 혼자 이렇게 풀었는데 시간초과가 떴다.
# 왜일까? 알고보니 13번째 줄에, min함수는 시간복잡도가 O(n)이라서 입력값이 최대 100,000인 이 문제에선 for문에 넣었기 때문에 시간초과가 뜨는 것이었다.
import sys
input=sys.stdin.readline
n=int(input())
edges = list(map(int, input().split()))
nodes = list(map(int, input().split()))
nodes.pop()

min_node = nodes[0]
ans = 0
for i in range(len(nodes)):
  if nodes[i] == min(nodes[i:]):
    ans += nodes[i] * sum(edges[i:])
    break
  else:
    if nodes[i] < min_node:
      min_node = nodes[i]
    ans += min_node * edges[i]
print(ans)


# 따라서 해당 if문을 그냥 지웠다. 생각해보니 꼭 필요한 구문은 아녔다
# 그래서 아래와 같이 제출했더니 맞았음
import sys
input=sys.stdin.readline
n=int(input())
edges = list(map(int, input().split()))
nodes = list(map(int, input().split()))
nodes.pop()

min_node = nodes[0]
ans = 0
for i in range(len(nodes)):
  if nodes[i] < min_node:
    min_node = nodes[i]
  ans += min_node * edges[i]
print(ans)
