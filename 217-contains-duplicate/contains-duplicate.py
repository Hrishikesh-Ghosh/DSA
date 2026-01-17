class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mp = {}
        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                return True
        return False
        