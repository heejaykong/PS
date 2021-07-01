# 모르겠어서 첨부터 다른 풀이 참고했다.(https://velog.io/@kgh732/Python-으로-푸는-Leetcode3.-Longest-Substring-Without-Repeating-Characters)
# Sliding Window 알고리즘이라고 함.
# 투포인터다.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      repeated = {}
      ans = 0
      left = 0
      for right, char in enumerate(s):
        if char in repeated and left <= repeated[char]:
          left = repeated[char] + 1
        else:
          ans = max(ans, right-left+1)
        repeated[char] = right # update existing char's index, or freshly add a new one to dictionary
      return ans
