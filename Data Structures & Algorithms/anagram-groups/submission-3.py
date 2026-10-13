class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sorted_S = ''.join(sorted(s)) #are we dealing w words that have the same chars?? if so, add!!
            res[sorted_S].append(s)
        return (list(res.values()))


