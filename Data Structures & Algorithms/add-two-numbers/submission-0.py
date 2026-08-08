# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = ""
        str2 = ""
        # Convert l1 into a string
        curr = l1
        while curr:
            str1 += str(curr.val)
            curr = curr.next
        # Convert l2 into a string
        curr = l2
        while curr:
            str2 += str(curr.val)
            curr = curr.next

        # Since the digits are backwards, reverse them
        total = int(str1[::-1]) + int(str2[::-1])
        # Convert answer back into reversed digits
        digits = str(total)[::-1]

        # Build linked list
        dummy = ListNode(0)
        curr = dummy

        for digit in digits:
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
        