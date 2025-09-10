from typing_extensions import Optional

class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val,
        self.next = next

def reverseListIteration(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next
        curr.next = prev

        prev = curr
        curr = nextNode

    return prev

def reverseListRecursion(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    rest = reverseListRecursion(head.next)

    head.next.next = head

    head.next = None

    return rest

def printList(node: Optional[ListNode]):
    while node is not None:
        print(f"{node.val}", end="")
        if node.next is not None:
            print(" -> ", end="")
        node = node.next
    print()

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    head = reverseListIteration(head)
    printList(head)
    head = reverseListRecursion(head)
    printList(head)