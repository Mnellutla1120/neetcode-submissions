class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []

        for p,s in zip(position,speed):
            t = (target - p) / s
            fleets.append(t)
        

        return(len(set(fleets)))