# 혼자 푼 버전
def countingValleys(steps, path):
  valley = 0
  alt = 0
  for step in path:
    if step == "U":
      alt += 1
    elif step == "D":
      alt -= 1

    if alt == 0 and step == "U":  # 수평선에 다다르고 마지막 step이 오르막길이었다면 valley다.
      valley += 1
  return valley
