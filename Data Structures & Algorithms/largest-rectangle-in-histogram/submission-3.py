class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
     stack = []
     #area = l * w
     #height[i] * (right - left + 1)
     heights = heights + [0]
     max_area = 0
     for r in range(len(heights)):
         while stack and heights[stack[-1]] > heights[r]:
                  pop_idx = stack.pop() 
                  l = stack[-1] if stack else -1
                  width = r - l  - 1
                  area = heights[pop_idx] * width
                  max_area = max(max_area,area)
         stack.append(r)

     return max_area

             


     


