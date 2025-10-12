# 3709. Design Exam Scores Tracker
# Medium

"""
intuition:
    since strictly increasing time, we can use binary search to find startTime and endTime
    maybe only start time and traverse through to find total

    prefix_sum can be used to instantly find the sum with 0(1) time
"""
class ExamTracker:
    def __init__(self):
            self.records: list[tuple[int, int]] = [(0, 0)]

    def record(self, time: int, score: int) -> None:
        self.records.append((time, score + self.records[-1][1]))

    def lowerBound(self, target: int) -> int:
        lo, hi = 0, len(self.records)

        while lo < hi:
            m = (lo + hi) // 2
            if self.records[m][0] >= target:
                hi = m
            else:
                lo = m + 1
        return lo

    def upperBound(self, target: int) -> int:
        lo, hi = 0, len(self.records)
        while lo < hi:
            m = (lo + hi) // 2
            if self.records[m][0] <= target:
                lo = m + 1
            else:
                hi = m
        return lo

    def totalScore(self, startTime: int, endTime: int) -> int:
        left = self.lowerBound(startTime)
        right = self.upperBound(endTime)

        if left == len(self.records) or right == 0:
            return 0

        return self.records[right - 1][1] - self.records[left - 1][1]

obj = ExamTracker()
obj.record(1, 99)
obj.record(2, 98)
obj.record(3, 100)
obj.record(4, 100)
obj.record(5, 100)
obj.record(6, 100)
obj.record(7, 100)

print(obj.totalScore(1, 1))
print(obj.totalScore(4, 7))
print(obj.totalScore(2, 10))
