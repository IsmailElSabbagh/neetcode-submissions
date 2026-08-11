class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1=[]
        list2=[]
        for i in s:
            list1.append(i)
        for j in t:
            list2.append(j)
        list1.sort()
        list2.sort()
        return True if list1 == list2 else False