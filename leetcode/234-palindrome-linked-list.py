# 234. Palindrome Linked List
# Easy
#
class ListNode:
    def __init__(self, val: int = 0) -> None:
        self.val: int = val
        self.next: ListNode | None

def isPalindrome(head: ListNode | None) -> bool:
    x: list[int] = []
    curr = head
    while curr:
        x.append(curr.val)
        curr = curr.next

    if x == x[::-1]:
        return True

    return False
