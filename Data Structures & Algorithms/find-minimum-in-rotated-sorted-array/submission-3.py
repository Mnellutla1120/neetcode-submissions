class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        while l < r:
            m = l + (r - l) // 2 #find middle
            if nums[m] < nums[r]:
                 r = m #when right is sorted, look left for pivot
            else:
                 l = m + 1 #left is sorted, so look right for pivot
        return nums[l]
        