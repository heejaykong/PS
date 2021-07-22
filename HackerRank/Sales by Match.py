# 혼자 풀어본 버전
# count 메소드를 쓰면 O(n**2)가 될 것 같아서 다음과 같이 O(n)으로 풀어 보았다.
def sockMerchant(n, ar):
  pair = 0
  cnt = 0
  sorted_ar = sorted(ar) # 오름차순으로 정렬하면 같은 숫자들끼리 모인다
  for i in range(len(sorted_ar)):
    if i>0:
      if sorted_ar[i] != sorted_ar[i-1]: # 이전 숫자와 다른 숫자면, pair 업데이트와 함께 cnt변수 초기화
        pair += cnt//2
        cnt = 0
    cnt += 1
    
  pair += cnt//2  # 마지막 원소까지 반영하기 위해 업뎃코드를 한줄 더 넣어야 하더라
  return pair
