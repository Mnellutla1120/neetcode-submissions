# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n > 0 and right:
             right = right.next
             n -= 1 #once n =0, we shifted by the necessary amt.
        while right:
            left = left.next #keep shifting left accordingly
            right = right.next
        # delete
        left.next = left.next.next #shift left pointer by 1, ignoring the middle node
        # 1 -> 2 -> 3 becomes 1--> 3

        return dummy.next
        
         




