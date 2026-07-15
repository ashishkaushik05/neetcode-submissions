import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num]+=1
            else:
                count[num] = 1
        
        heap = []
        for num in count:
            heap.append((-count[num] , num))
        heapq.heapify(heap)

        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])

        return result