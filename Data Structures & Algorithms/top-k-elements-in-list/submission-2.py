from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        freq_map = Counter(nums)
        

        for number,count in freq_map.items():
            if count >= k:
                res.append(number)
        
        return res

