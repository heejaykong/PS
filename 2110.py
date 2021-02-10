# https://velog.io/@seanlion/boj2110
# https://assaeunji.github.io/python/2020-05-07-bj2110/
# https://claude-u.tistory.com/448

import sys
houseCount, fixedWifiCount = map(int, sys.stdin.readline().split())
houses = sorted([int(sys.stdin.readline()) for i in range(houseCount)])

shortest = 1
longest = houses[-1]-houses[0]

def routerCount(distance):
  startIndex = 0
  count = 1
  for i in range(1,len(houses)):
    if houses[i] >= houses[startIndex]+distance:
      count += 1
      startIndex = i
  return count

answer = 0
while shortest <= longest:
  midDistance = (shortest+longest)//2
  wifiCount = routerCount(midDistance)
  if wifiCount >= fixedWifiCount:
    # 거리를 넓혀야 함
    shortest = midDistance + 1
    answer = midDistance
  else:
    # 거리를 좁혀야 함
    longest = midDistance - 1
print(answer)
