import heapq

class TaskManager:

    def __init__(self, tasks):
        # taskId → [userId, priority]
        self.task_info = {}

        # max heap: store (-priority, -taskId) so highest priority/taskId pops first
        self.heap = []

        for userId, taskId, priority in tasks:
            self.add(userId, taskId, priority)

    def add(self, userId, taskId, priority):
        self.task_info[taskId] = [userId, priority]
        heapq.heappush(self.heap, (-priority, -taskId))

    def edit(self, taskId, newPriority):
        # just update the map — old heap entry becomes stale
        # push new entry, lazy deletion handles the rest in execTop
        self.task_info[taskId][1] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId))

    def rmv(self, taskId):
        # just remove from map — heap entry becomes stale
        del self.task_info[taskId]

    def execTop(self):
        while self.heap:
            neg_pri, neg_tid = heapq.heappop(self.heap)
            taskId = -neg_tid
            priority = -neg_pri

            # skip if task was deleted or priority changed (stale entry)
            if taskId not in self.task_info:
                continue
            if self.task_info[taskId][1] != priority:
                continue

            # valid task — execute it
            userId = self.task_info[taskId][0]
            del self.task_info[taskId]
            return userId

        return -1  # no tasks left