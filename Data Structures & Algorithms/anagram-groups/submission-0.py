class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        for string in strs:
            my_word = str(sorted(string))

            if my_word not in hashmap:
                hashmap[my_word] = [string]
            else:
                hashmap[my_word].append(string)

        return list(hashmap.values())
            



        