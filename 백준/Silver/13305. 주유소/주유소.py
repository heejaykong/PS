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
    else:
      ans += min_node * edges[i]
print(ans)
