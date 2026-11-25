class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0,len(height) - 1
        leftMax, rightMax = height[0], height[-1]
        water = 0
        #trapped if its between two masses of land
        #prefix and suffix approach
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

