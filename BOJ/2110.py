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
  if wifiCount >= fixedWifiCount:  # 공유기를 목표치 이상으로 설치할 수 있다면, 정답이 될 수 있음. 이 부분 이해 안 가는 건 https://blog.naver.com/pjok1122/221652210187 참고("잘 생각해보면, 공유기의 갯수가 C와 일치하더라도, 공유기의 '간격(mid)'을 좀 더 크게 설치해볼 필요성이 있다.")
    # 거리를 넓혀야 함
    shortest = midDistance + 1
    answer = midDistance
  else:
    # 거리를 좁혀야 함
    longest = midDistance - 1
print(answer)
