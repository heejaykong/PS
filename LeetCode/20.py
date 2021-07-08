# 혼자 풀어본 버전. 딕셔너리를 이용해서 괄호의 짝꿍을 판별했다. 퍼포먼스는 좀 많이 안 좋은 편이라 개선점을 아래 찾아봤다.
class Solution:
  def isValid(self, s: str) -> bool:
    d = {"(":")", "{":"}", "[":"]"}
    stack = []
    for item in s:
      # 우선 스택에 아무것도 없으면 무조건 푸쉬
      if len(stack) == 0: stack.append(item)
      # 그 다음부턴 짝꿍이 맞는지 확인하며 팝 또는 푸쉬
      else:
        if stack[-1] in d and d[stack[-1]] == item:
          stack.pop()
        else:
          stack.append(item)
    # 전부 실행한 다음 스택에 뭐가 있으면 False, 없으면 True
    if len(stack) == 0:
      return True
    else:
      return False

# 다른 답안 참고하고 개선한 버전
