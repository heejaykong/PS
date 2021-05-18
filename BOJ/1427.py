stack=list(input())
stack.sort(reverse=True)
print(''.join(stack))

# 또는
print(''.join(sorted(input(), reverse=True)))

# sorted()과 sort()의 차이:
# sorted(something)는 새로운 리스트를 반환한다 && list가 아닌 object도 sort 가능하다
# some_list.sort()는 기존 리스트를 변경한다 && 오로지 list에만 사용 가능하다
