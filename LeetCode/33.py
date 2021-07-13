# 처음엔 덱 rotate 이용해서 풀었는데,
# 일부 테스트케이스가 통과 안되는 거 처리하려니까 복잡해지고 번거로워지길래 맞는 방법이 아닌 것 같아서
# 결국 다른 모법답안 보고 풀었다. (https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms)
class Solution:
  def search(self, nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
      mid = (low + high) // 2
      if nums[mid] == target:
        return mid
      
      # list:  [ 0,  1,  2,  3,  4,  5,  6 ]
      # index:  [4] [5] [6] [0] [1] [2] [3]
      # 위와 같다고 칠 때,
      
      # mid가 오른쪽에 위치할 경우
      if nums[low] <= nums[mid]:
        if nums[low] <= target <= nums[mid]:
          high = mid # 범위 내에 있으니까
        else:
          low = mid + 1 # 범위 바깥이니까
      
      # mid가 왼쪽에 위치할 경우
      else:
        if nums[mid] <= target <= nums[high]:
          low = mid
        else:
          high = mid - 1
      
    return -1
