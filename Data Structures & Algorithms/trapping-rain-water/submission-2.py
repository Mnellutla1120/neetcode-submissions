class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        leftMax = 0
        rightMax = 0
        water = 0
        #trapped if its between two masses of land
        while l < r:
             if height[l] < height[r]:
                 l += 1
                 leftMax = max(leftMax,height[l])
                 water += (leftMax - height[l])
             else:
                 r -= 1
                 rightMax = max(rightMax,height[r])
                 water += (rightMax - height[r])
        return water

