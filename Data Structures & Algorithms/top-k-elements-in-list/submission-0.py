class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)] #updated based on our array

        for n in nums:
             count[n] = 1 + count.get(n,0)
        for n, c in count.items(): #key-value pair for dict
             freq[c].append(n) #this value n occurs c # of times
        res = []
        for i in range(len(freq)-1,0,-1): #go desc order
            for n in freq[i]:
                 res.append(n) #get n-value that occurs most freq.
                 if len(res) == k:
                     return res
        






    


            
        