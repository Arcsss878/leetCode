# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        headPointer = ListNode(0)
        current = headPointer
        carry = 0

        while l1 or l2 or carry:
            current.next = ListNode(0)
            current = current.next

            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            
            current.val = carry % 10
            carry //= 10

        return headPointer.next
        