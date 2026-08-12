class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        n = len(people)
        people.sort()
        boat_counter = 0
        i = 0
        j = len(people) - 1

        while i <= j:
             boat_counter += 1 #irrespective of if the boat is for one or two ppl, we need a boat
             if people[i] + people[j] <= limit:
                 i += 1
                 j -= 1
             else:
                 j -= 1

        return boat_counter
            


            




      
