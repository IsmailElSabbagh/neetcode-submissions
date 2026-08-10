class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest_one=0
        counter=0
        for i in range(len(nums)):
            if nums[i] == 1:
                counter+=1
                if counter > longest_one:
                    longest_one=counter
            else:
                counter = 0
        return longest_one

        