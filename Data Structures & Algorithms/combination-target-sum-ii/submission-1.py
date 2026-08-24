class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()


        def dfs(start, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            

            if total > target:
                return 
            
            for j in range(start, len(candidates)):
                if j > start and candidates[j - 1] == candidates[j]:
                     continue
                cur.append(candidates[j])
                dfs(j + 1, cur, total + candidates[j])
                cur.pop()
            
        
        dfs(0,[],0)
        return res
        




    


