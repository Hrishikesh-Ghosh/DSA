class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        nums_set = set(nums)
        for x in nums_set:
            if (x-1) in nums_set:
                continue
            else:
                count = 1
                length = 1
                while (x + length) in nums_set:
                    count += 1
                    length += 1
                if count >= max_count:
                     max_count = count
        return max_count
                