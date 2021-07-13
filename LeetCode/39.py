# 짱 열심히 풀었는데 또 일부 테스트케이스가 통과를 안해서 확인해보니.. 모든 경우의 수를 탐색하지 못한 알고리즘인 걸 깨달았다.
# 그래서 찾아보니 걍 dfs 문제였음. dfs/bfs 문제 좀 찾아서 각잡고 풀어봐야겠다...
# 참고 답안: https://leetcode.com/problems/combination-sum/discuss/16510/Python-dfs-solution./
class Solution:
  def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    ans = []
    self.dfs(candidates, target, [], ans)
    return ans

  def dfs(self, nums, target, path, ans):
    if target < 0:
      return
    if target == 0:
      ans.append(path)
      return
    
    for i in range(len(nums)):
      if target < nums[i]: break
      self.dfs(nums[i:], target-nums[i], path+[nums[i]], ans)
