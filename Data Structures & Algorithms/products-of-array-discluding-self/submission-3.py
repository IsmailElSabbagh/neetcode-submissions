class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1] * len(nums) #output [1,1,1,1,...n]

        for i in range(len(nums)):
            if i < len(nums)-1:
                res[i+1]=res[i]*nums[i]
        #res has prefixes now we add the postfixes
        intermediate_int=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=intermediate_int 
            intermediate_int*=nums[j]
        return res




        """
        First try has a too high time complexity
        hashmap={}

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i !=j:
                    if i in hashmap:
                        hashmap[i]*=nums[j]
                    else:
                        hashmap[i] = nums[j] 
        return list(hashmap.values())
        """
            