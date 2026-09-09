class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for c in details:
            if int(c[11])*10 + int(c[12]) > 60:
                count += 1
        
        return count
                