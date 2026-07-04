class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        HashMap = {}
        for i in nums:
            HashMap[i] = HashMap.get(i,0) + 1
            if HashMap[i] > 1:
                return True
        return False