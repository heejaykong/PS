import sys
houseCount, wifiCount = map(int, sys.stdin.readline().split())
houses = sorted([int(sys.stdin.readline()) for i in range(houseCount)])

start = 1
end = houses[-1] - houses[0]

def predictWifiCount(distance):
    markedPlace = 0
    count = 1
    for i in range(1, len(houses)):
        if houses[markedPlace] + distance > houses[-1]:
            break
        elif houses[markedPlace] + distance <= houses[i]:
            count += 1
            markedPlace = i
    return count

answer = 0
while start <= end:
    mid = (start + end)//2
    count = predictWifiCount(mid)
    if count >= wifiCount:
        answer = mid
        start = mid + 1
    else:
        end = mid -1
print(answer)