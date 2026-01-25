class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []
        nums.sort()
        for i, v in enumerate(nums):
            if nums[i] == nums[i-1] and i>0:
                continue
            left = i+1
            right = len(nums) - 1
            while left<right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]]) 
                    left+=1
                    while nums[left] == nums[left-1] and left<right:
                        left+=1
        return output

        