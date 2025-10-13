# 160. Intersection of Two Linked Lists
# Easy

class ListNode:
    def __init__(self, x: int) -> None:
        self.val: int = x
        self.next: ListNode | None = None



def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode | None:
    one = headA
    two = headB

    while one != two:
        one = headB if one is None else one.next
        two = headA if two is None else two.next

    return one
