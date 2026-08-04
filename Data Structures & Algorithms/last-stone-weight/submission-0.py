class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
     stones = [-s for s in stones]
     heapq.heapify(stones) #make heap!!

     while len(stones) > 1:
         first = heapq.heappop(stones)
         second = heapq.heappop(stones)
         if second > first: #do the opposite since its neg now
             heapq.heappush(stones, first - second)
     stones.append(0)
     return abs(stones[0]) #our last remaining stone in our heap
