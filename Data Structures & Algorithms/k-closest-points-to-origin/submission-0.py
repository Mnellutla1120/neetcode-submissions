class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #1: create a heap of all of our euclidian distances
        # (sqrt((x1 - x2)^2 + (y1 - y2)^2))
        h = []
        for p in points:
            dis = math.sqrt((p[0] - 0)**2 + (p[1] - 0)**2)
            h.append((dis,p))
        heapq.heapify(h)
        res = []
        if len(points) == 0: #base case: list is empty
             return [[]]
        if len(points) == 1: #base case, we only have one point
             return [points[0]]
        
        while len(res) < k:
             distance,point = heapq.heappop(h)
             res.append(point)
  
         
        
        
        return res


