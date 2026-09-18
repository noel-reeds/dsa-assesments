# definition of a Linkedlist
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value=value
        self.next=next

def reverse3(node: ListNode):
    if node.next:
        reverse3(node.next)
        print(node.value)
    else:
        print(node.value)
        return
