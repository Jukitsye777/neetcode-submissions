class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxheap = [-cnt for cnt in count.values()]
        heapq.heapify(maxheap)
        time = 0

        queue = deque()

        while maxheap or queue:
            time += 1
            if maxheap:
                task =1+  heapq.heappop(maxheap)
                if task:
                    queue.append([task,time+n])


            if queue and queue[0][1] == time:
                heapq.heappush(maxheap,queue.popleft()[0])

        return time



