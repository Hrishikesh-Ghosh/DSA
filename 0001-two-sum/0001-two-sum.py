class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        for i in range(len(nums)):
            HashMap[i] = nums[i]
        for i in HashMap:
            for j in HashMap:
                if i != j and HashMap[i]+HashMap[j]==target:
                    return i, j
                else:
                    continue 
        