# Kadane's algorithm이라고 한다. DP문제다
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    curSum = maxSum = nums[0]
    for num in nums[1:]:
      curSum = max(num, curSum + num)
      maxSum = max(maxSum, curSum)

    return maxSum
