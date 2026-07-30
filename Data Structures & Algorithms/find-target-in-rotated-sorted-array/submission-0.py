class Solution:
    def search(self, nums: List[int], target: int) -> int:
         l,r = 0, len(nums) - 1
         while l <= r:
             mid = (l + r) // 2
             if nums[mid] == target:
                 return mid
             if nums[l] <= nums[mid]:
             #left half sorted...
                if nums[l] <= target:
                     r = mid-1
                else:
                     l = mid + 1
             else:
             #right is sorted...
                if nums[mid] < target:
                     l = mid + 1
                else:
                     r = mid - 1
         return -1




        