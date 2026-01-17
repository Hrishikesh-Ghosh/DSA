class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0]*len(nums)

        prefix_var = 1
        for i in range(len(nums)):
            result[i] = prefix_var
            prefix_var *= nums[i]

        postfix_var = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix_var
            postfix_var *= nums[i] 
        
        return result 