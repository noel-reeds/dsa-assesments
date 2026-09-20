# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if l1.next or l2.next:
            if l2.val + l1.val > 10:
                node = ListNode(0, l1.next)
                l1.next.val += 1
                addTwoNumbers(self, l1.next, l2.next)
            sumNode.val = l1.val + l2.val
        else:
            node = ListNode(l2.val + l1.val, None)
