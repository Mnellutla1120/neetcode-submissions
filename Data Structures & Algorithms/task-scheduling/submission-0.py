class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:   
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque() #pairs of [-cnt, idleTime]

        while maxHeap or q: #we have more tasks that we need to process
             time += 1
             if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap) #make more pos aka more max
                if cnt:
                   q.append([cnt,time + n])
             if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
                


            





       
             

