class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """

        self.minheap= nums
        self.k = k

        heapq.heapify(self.minheap)

        while(len(self.minheap)>k):
            heapq.heappop(self.minheap)

        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """

        heapq.heappush(self.minheap,val)
        if(len(self.minheap)>self.k):
            heapq.heappop(self.minheap)
        return self.minheap[0]
        
