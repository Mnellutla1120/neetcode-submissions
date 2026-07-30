class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l,r = 0,len(numbers)-1

        while l < r: 
              if numbers[l] + numbers[r] < target:
                  l += 1 #get big num
              elif numbers[l] + numbers[r] > target:
                  r -= 1 #get smaller num
              else: 
                  res.append(numbers[l])
                  res.append(numbers[r])
                  return res
    
      

