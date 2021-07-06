# 다른 답안 참고함
# 투포인터 활용
class Solution:
  def threeSum(self, nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    N = len(nums)
    
    for i in range(N):
      if i>0 and nums[i]==nums[i-1]: continue   # i 중복 거르기
      left = i+1
      right = N-1

      while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
          left += 1
        elif sum > 0:
          right -= 1
        else:
          ans.append([nums[i], nums[left], nums[right]])
          while left<right and nums[left] == nums[left+1]: left += 1   # left 중복 거르기
          while left<right and nums[right] == nums[right-1]: right -= 1   # left 중복 거르기
          left += 1
          right -= 1
    return ans
