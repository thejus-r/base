from typing_extensions import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hare and Tortoise Algorithm
# One Fast Pointer and One Slow Pointer
# In this case, slow pointer move 1 node at a time, and fast pointer moves two node at a time
def hasCycle(head: Optional[ListNode]) -> bool:
    fast = head

    while head and head.next:
        head = head.next
        fast = fast.next.next

        if head == fast:
            return True
    return False