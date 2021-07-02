# 혼자 푼 버전
# 리트코드에서 제공하는 힌트를 좀 참고하긴 함
# 투포인터를 사용해, 가장 바깥쪽 양끝단부터 시작해서, 양끝단 중 min값보다 더 큰 값이 안에 존재하면, 안으로 좁혀가는 식이다.
class Solution:
  def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height)-1
    ans = min(height[left], height[right]) * (right - left)

    while left < right:
      # Who goes first? The shorter side pointer goes first.
      if height[left] < height[right] and left < right: # If the left side is sorter, left pointer goes first.
        current_height = height[left]
        while height[left] <= current_height:
          left += 1

      else:
        current_height = height[right]
        while height[right] <= current_height and left < right:
          right -= 1

      # Now we are holding the higher left OR right.
      volume = min(height[left], height[right]) * (right - left) # Measure the volume,
      ans = max(ans, volume) # and update!
    return ans
