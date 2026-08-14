class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)
        people.sort()
        boat_counter = 0
        l = 0
        r = n - 1

        while l <= r:
         boat_counter += 1
         if people[l] + people[r] <= limit:
             l += 1
             r -= 1
             
         else:
             r -= 1 #too many ppl 
        return boat_counter






        


            




      
