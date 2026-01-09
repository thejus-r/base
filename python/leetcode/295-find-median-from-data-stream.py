# 295. Find Median from Data Stream
# Hard

"""
Dry Run
1 <- top (keeps track of upper)
2 <- bottom (keeps track of lower)

1
2
3

1
2 <- top (keeps track of upper) (maxHeap)
3 <- bottom (keeps track of lower) (minHeap)
4

"""
from heapq import heappop, heappush
class MedianFinder:

    def __init__(self) -> None:
        self.top = [] # maxHeap (negated)
        self.bottom = [] # minHeap

    def addNum(self, num: int) -> None:
        heappush(self.top, -num)

        val = -heappop(self.top)
        heappush(self.bottom, val)

        # balance the heaps
        if len(self.bottom) > len(self.top):
            val = heappop(self.bottom)
            heappush(self.top, -val)

    def findMedian(self) -> float:
        # odd number to element, we store the middle in the top
        if len(self.top) > len(self.bottom):
            return -self.top[0]
        else:
            return (-self.top[0] + self.bottom[0]) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())
    mf.addNum(3)
    print(mf.findMedian())
