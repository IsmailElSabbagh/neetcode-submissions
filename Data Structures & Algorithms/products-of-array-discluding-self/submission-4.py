class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res=[1] * len(nums) #output [1,1,1,1,...n]
        #removed the if statement and added the prefix = 1 to save computation time 
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        #res has prefixes now we add the postfixes
        #theoretically we could discard the postfix and prefix and make a common variable to save space 
        postfix=1
        for j in range(len(nums)-1,-1,-1):
            res[j]*=postfix
            postfix*=nums[j]
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
            