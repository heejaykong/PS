# 브루트 포스로 푼 버전
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)-1):
      for j in range(i+1, len(nums)):
        temp = nums[i] + nums[j]
        if temp == target:
          return [i, j]

# 더 개선한 버전(자기 짝꿍(target-nums[i])을 딕셔너리에 적어놓고 가는 시스템)
class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    vals = {}
    for i in range(len(nums)):
      if nums[i] in vals:
        return [i, vals[nums[i]]]
      vals[target - nums[i]] = i
