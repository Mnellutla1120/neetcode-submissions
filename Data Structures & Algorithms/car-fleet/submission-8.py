class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = sorted(zip(position,speed),reverse=True)
        stack = []
        for p,s in fleets:
             t = (target - p) / s
             if not stack or t > stack[-1]:
                 stack.append(t)
        return(len(stack))