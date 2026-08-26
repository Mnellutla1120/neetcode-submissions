class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
           res = [0] * len(arr)
           r_max = -1

           for i in range(len(arr)-1,-1,-1):
                 res[i] = r_max
                 r_max = max(r_max,arr[i])
           return res