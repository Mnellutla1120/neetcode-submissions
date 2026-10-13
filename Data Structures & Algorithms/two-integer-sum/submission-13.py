class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1

        while l < r:
            if abs(nums[l]) + abs(nums[r]) == target:
                return [l,r]
            if abs(nums[l]) + abs(nums[r]) > target:
                r -= 1
            if abs(nums[l]) + abs(nums[r]) < target:
                l += 1
        return [l,r]
            