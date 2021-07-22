# 쉬웠다..
def repeatedString(s, n):
  return (n // len(s)) * s.count("a") + s[ : n % len(s)].count("a")

# 가독성 좋은 버전
def repeatedString(s, n):
  a_count_in_s = s.count("a")
  regular_s_count = n // len(s) * a_count_in_s
  substring_s_count = s[:n % len(s)].count("a")
  
  ans = regular_s_count + substring_s_count
  return ans
