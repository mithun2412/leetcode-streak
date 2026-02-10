import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        # Step 1: push all stones as negative values
        for s in stones:
            heapq.heappush(heap, -s)

        # Step 2: keep smashing two largest stones
        while len(heap) > 1:
            y = -heapq.heappop(heap)  # largest
            x = -heapq.heappop(heap)  # second largest

            if y != x:
                heapq.heappush(heap, -(y - x))

        # Step 3: result
        return -heap[0] if heap else 0
