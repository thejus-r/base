from typing_extensions import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Hare and Tortoise Algorithm
# One Fast Pointer and One Slow Pointer
# In this case, slow pointer move 1 node at a time, and fast pointer moves two node at a time
def detectCycle(head: Optional[ListNode]) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None