class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i in range(len(nums)):
            number= target-nums[i]
            if number in hashmap:
                return [hashmap[number],i]
            hashmap[nums[i]]= i    
