# definition of a Linkedlist
class ListNode(object):
    def __init__(self, value=0, next=None):
        self.value=value
        self.next=next

def traverse_linkedlist(node: ListNode):
    if node.next:
        print(node.value)
        reverse3(node.next)
    else:
        print(node.value)
        return
