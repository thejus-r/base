class Heap:
    def __init__(self) -> None:
        self.list = []

    def __swap(self, f, s):
        temp = self.list[f]
        self.list[f] = self.list[s]
        self.list[s] = temp

    def __parent(self, idx):
        return (idx - 1)// 2

    def __left(self, idx):
        return (idx * 2) + 1

    def __right(self, idx):
        return (idx * 2) + 2

    def __upheap(self, idx):
        if idx == 0:
            return
        p = self.__parent(idx)
        if self.list[idx] < self.list[p]:
            self.__swap(idx, p)
            self.__upheap(p)

    def insert(self, val):
        self.list.append(val)
        self.__upheap(len(self.list) - 1)

    def remove(self, val):
        if len(self.list) < 1: return

        temp = self.list[0]
        last = self.remove(len(self.list) - 1)
        if (len(self.list) > 0):
            self.list[0] = last

        return temp


h = Heap()
h.insert(1)
h.insert(2)
h.insert(3)
h.insert(1)
h.insert(-1)

print(h.list)
