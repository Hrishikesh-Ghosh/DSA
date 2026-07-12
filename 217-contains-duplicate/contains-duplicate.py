class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        Hashmap = {}
        for i in nums:
            Hashmap[i] = Hashmap.get(i,0)+1
            if Hashmap[i] == 1:
                continue
            else:
                return True
        return False
