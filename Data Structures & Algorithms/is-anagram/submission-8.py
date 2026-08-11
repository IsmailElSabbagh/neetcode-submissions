class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmapS, hashmapT = {}, {}
        for i in range(len(s)):
            hashmapS[s[i]] =  1+ hashmapS.get(s[i],0)
            hashmapT[t[i]] = 1+ hashmapT.get(t[i],0)
        
        for c in hashmapS:
            if hashmapS[c] != hashmapT.get(c, 0):
                return False 
        return True 


        """
        class Solution:
            def isAnagram(self, s: str, t: str) -> bool:
                if len(s) != len(t):
                    return False
        
                s_map = {}
                t_map = {}
                for i,j in zip(s,t):
                if i in s_map:
                    s_map[i] += 1
                else:
                    s_map[i] = 0

                if j in t_map:
                    t_map[j] += 1
                else:
                    t_map[j] = 0
        
            return s_map == t_map
        """
