class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            # Step 1: Count frequency
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Step 2: Use min heap of size k
        heap = []
        
        for num, count in freq.items():
            heappush(heap, (count, num))
            
            if len(heap) > k:
                heappop(heap)

        # Step 3: Extract elements
        result = []
        while heap:
            result.append(heappop(heap)[1])

        return result