from collections import deque, defaultdict
from typing import List
class Router:
    def __init__(self, memoryLimit: int) -> None:
        self.buffer = deque()
        self.dest = defaultdict(list)
        self.memoryLimit = memoryLimit
        self.exist = set()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.exist:
            return False
        self.buffer.append(f'{source}_{destination}_{timestamp}')
        self.exist.add((source, destination,timestamp))
        self.dest[destination].append(timestamp)

        if len(self.buffer) > self.memoryLimit:
            self.forwardPacket()

        return True

    def forwardPacket(self) -> List[int]:
        if self.buffer:
             firstPacket = self.buffer.popleft()
             source, destination,timestamp = map(int,firstPacket.split('_'))
             self.exist.discard((source, destination,timestamp))
             self.dest[destination].pop(0)
             return [source, destination,timestamp]
        else:
            return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        l, r = 0, len(self.dest[destination])-1
        lt = self.dest[destination]

        while l <= r:
            m = (l + r) // 2
            if lt[m] >= startTime:
                r = m - 1
            else:
                l = m + 1
        leftBound = l
        l,r = 0, len(self.dest[destination])-1
        while l <= r:
            m = (l + r) // 2
            if lt[m]<=endTime:
                l = m+1
            else:
                r = m-1
        rightBound = r
        return rightBound-leftBound+1

router = Router(3)
router.addPacket(1, 4, 90) # True
router.addPacket(2, 5, 90) # True
router.addPacket(1, 4, 90) # False
router.addPacket(3, 5, 95) # True
router.addPacket(4, 5, 105) # True
router.forwardPacket() # [2, 5, 90]
router.addPacket(5, 2, 110) # True
print(router.getCount(5, 100, 110)) # 1
print(router.buffer)
