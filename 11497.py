import sys

T = int(sys.stdin.readline())

def showDiff(trees, treeCount):
  biggest = 0
  for i in range(treeCount):
    if i+2 <= len(trees)-1:
      diff = abs(trees[i] - trees[i+2])
      if diff > biggest:
        biggest = diff
  print(biggest)

for i in range(T):
  treeCount = int(sys.stdin.readline())
  trees = sorted(list(map(int, sys.stdin.readline().split())))
  showDiff(trees, treeCount)
