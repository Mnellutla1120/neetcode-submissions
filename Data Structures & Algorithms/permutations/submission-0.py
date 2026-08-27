class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()

        def dfs(curr, seen):
            if len(curr) == len(nums):
                 res.append(curr.copy())
                 return 
            for num in nums:
                if num not in seen:
                     curr.append(num)
                     seen.add(num)
                     dfs(curr,seen)
                     curr.pop()
                     seen.remove(num)

        
        dfs([],seen)
        return res