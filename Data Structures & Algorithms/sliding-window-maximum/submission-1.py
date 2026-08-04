from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
         heap = [] #max heap implemented w neg vals (-val, index)
         output = []
         for i in range(len(nums)):
            #add curr elem + first index to heap
            heapq.heappush(heap,(-nums[i],i))
            #wait until we formed first current window
            if i >= k - 1:
                #remove elems from top if they slid out window
                #curr window: [i - k + 1, ..., i]
                while heap[0][1] <= i - k:
                     heapq.heappop(heap)
                #top of heap = largest valid element
                output.append(-heap[0][0])
         return output





   
        

     
  
            

  
