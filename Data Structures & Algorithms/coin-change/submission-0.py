class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #base case
        if amount == 0:
            return 0
        
        q = deque([0])
        #visited
        seen = [False] * (amount + 1)
        seen[0] = True
        res = 0

        while q:
            res += 1
            for _ in range(len(q)):
                #process nodes
                cur = q.popleft()
                for c in coins:
                    nxt = cur + c
                    if nxt == amount:
                         return res
                    if nxt > amount or seen[nxt]:
                         continue
                    seen[nxt] = True
                    q.append(nxt)
        return -1

            
            
        