from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #kth most frequent, first most frequent would be our 0th element, 2nd most freq is our 1st indexed element, so we want the k-1th index

        res = []
        max_h = []
        freq_map = Counter(nums)
        for number, count in freq_map.items(): #make a max heap, now we must retrieve our kth most common element
            heapq.heappush(max_h, (-count,number))
        
        for i in range(k): #go up to k-1
            element = heapq.heappop(max_h)
            res.append(element[1])
        
        
        return res
        
        
        


