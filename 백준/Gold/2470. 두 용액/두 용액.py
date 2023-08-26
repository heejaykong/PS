import math
T = int(input())
items = list(map(int, input().split()))
min = math.inf
i = 0
j = T-1
item1, item2 = 0, 0
items.sort()
while 1:
  current = items[i] + items[j]
  if abs(min) > abs(current):
    min = current
    item1 = i
    item2 = j
  if (current<0):
    i+=1
  else:
    j=j-1
  if j<=i:
    break
print(items[item1], items[item2])