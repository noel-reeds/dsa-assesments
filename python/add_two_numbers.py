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
                x = l2.val + l1.val
                node = ListNode(x % 10, l1.next if l1.next else l2.next)
                l1.next.val += 1
                addTwoNumbers(self, l1.next, l2.next)
            else:
                node = ListNode(l2.val + l1.val, l1.next if l1.next else l2.next)
                addTwoNumbers(self, l1.next, l2.next)
        else: # if each linkedlist has one node.
            if l2.val + l1.val > 10:
                x = l2.val + l1.val
                n2 = ListNode(x % 10, None)
                n3 = ListNode(1, n2)
            else:
                n5 = ListNode(l2.val + l1.val, None)
        return node
