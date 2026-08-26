class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for string in strs:
            count= [0] * 26 #sequence/fingerprint/key for each word just a list made out of zeros 
            for c in string:
                count[ord(c) - ord("a")] +=1
            res[tuple(count)].append(string)
        return list(res.values()) 
            



        