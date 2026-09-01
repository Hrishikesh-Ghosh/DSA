class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        answer_arr = []
        for index, value in enumerate(nums):
            hashmap[index] = value
        for i in hashmap:
            for j in hashmap:
                if i == j:
                    continue
                if hashmap[i] + hashmap[j]  == target:
                    return i,j

        