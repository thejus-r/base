from typing import List
import heapq
class TaskManager:
    def __init__(self, tasks: List[List[int]]) -> None:
        self.maxHeap = []
        self.taskMap = {}

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.taskMap[taskId] = (userId, priority)
        heapq.heappush(self.maxHeap, (-priority, -taskId))

    def edit(self, taskId:int , newPriority: int) -> None:
        if taskId in self.taskMap:
            userId, _ = self.taskMap[taskId]
            self.taskMap[taskId] = (userId, newPriority)
            heapq.heappush(self.maxHeap, (-newPriority, -taskId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.taskMap:
            del self.taskMap[taskId] # only deleting in lookup table, task is lazy deleted from heap while execution

    def execTop(self) -> int:
        while self.maxHeap:
            priority, taskId = heapq.heappop(self.maxHeap)
            taskId = -taskId
            priority = -priority
            if taskId in self.taskMap and self.taskMap[taskId][1] == priority:
                userId, _ = self.taskMap[taskId]
                del self.taskMap[taskId]
                return userId
        return -1


task = TaskManager([[1, 101, 10], [2, 102, 20], [3, 103, 15]])
task.add(4, 104, 5)
task.edit(102, 8)
print(task.execTop())
task.rmv(101)
task.add(5, 105, 15)
print(task.execTop())