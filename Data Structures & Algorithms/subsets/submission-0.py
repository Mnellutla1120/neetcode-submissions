class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        subset = []

        for num in nums:
            res += [subset + [num] for subset in res]

        return res



        