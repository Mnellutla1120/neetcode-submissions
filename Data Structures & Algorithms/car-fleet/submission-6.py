class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
  
        for p,s in sorted(zip(position,speed),reverse=True):
            t = (target - p) / s
            fleets.append(t)
        

        return(len(set(fleets)))