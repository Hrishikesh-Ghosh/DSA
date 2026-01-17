class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mp = {}
        v = 0
        for i in nums:
            mp[v] = i
            v += 1
        for i in mp:
            for j in mp:
                if i == j:
                    continue
                else:
                    if mp[i] + mp[j] == target:
                        return [i,j]

            