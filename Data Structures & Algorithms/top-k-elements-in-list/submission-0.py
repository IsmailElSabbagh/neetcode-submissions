class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for number in nums:
            if number not in hashmap:
                hashmap[number] = 1
            else:
                hashmap[number] += 1

        my_result = []

        for i in range(k):
            max_key = max(hashmap, key=hashmap.get)
            my_result.append(max_key)
            del hashmap[max_key]

        return my_result