class Node:
    def __init__(self, value: int | None = None, next: Node | None = None) -> None:
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self) -> None:
        self.root = Node()
        self.size = 0

    def append(self, value: int) -> None:
        curr = self.root

        while curr.next:
            curr = curr.next

        curr.next = Node(value)
        self.size += 1

    def find(self, value: int) -> int:
        curr = self.root.next

        i = 0
        while curr:
            if curr.value == value:
                return i
            curr = curr.next
            i += 1

        return -1

    def display(self) -> None:
        curr = self.root.next
        print("ROOT |-> ", end="")

        while curr:
            print(f"{curr.value}", end=" -> ")
            curr = curr.next

        print("END \n")


if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(2)
    sl.append(4)
    sl.append(7)
    sl.append(6)

    sl.display()
    print("Size: ", sl.size)
    print("Find 2: ", sl.find(2))
    print("Find 7: ", sl.find(7))
    print("Find 1: ", sl.find(1))
