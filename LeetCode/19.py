# 혼자 풀어본 버전

# Definition for singly-linked list.
# class ListNode:
#   def __init__(self, val=0, next=None):
#     self.val = val
#     self.next = next

class Solution:
  def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    
    temp = head
    # length 먼저 알아내기
    length = 0
    while temp != None:
      length += 1
      temp = temp.next
    
    temp = head
    index_to_delete = length - n
    
    # 노드가 한개밖에 없거나 지우고자 하는 게 첫번째 노드일때
    if index_to_delete <= 0:
      head = head.next
      return head
    
    # 그 외에는 해당 노드까지 가서 그 노드 삭제하기
    while temp != None:
      if index_to_delete == 1:
        # 삭제돼야 하는 노드(temp2)의 직전 노드(temp)를 다다음 노드와 연결해서 삭제
        temp2 = temp.next
        temp.next = temp2.next
        # 삭제된 노드의 next도 끊기
        temp2.next = None
        break
      else:
        index_to_delete -= 1
        temp = temp.next
    
    return head
