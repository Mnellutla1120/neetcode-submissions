class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) - 1
        area = (r - l) * min(heights[l], heights[r])
        max_a = area #curr_area
        while l < r:
            if heights[l] < heights[r]:
                     l += 1
            elif heights[r] < heights[l]:
                     r -= 1
            else: #its like a square, j get the area
                  l += 1

            area = (r - l) * min(heights[l], heights[r])
            max_a = max(max_a,area)
        return max_a
        