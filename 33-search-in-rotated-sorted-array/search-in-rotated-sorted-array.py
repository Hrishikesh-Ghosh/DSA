class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums)-1
        while L<=R:
            M = (L + R) // 2
            if nums[M] == target:
                return M
            else:
                if nums[M] > nums[R]: 
                    if target <= nums[R]:
                        L = M+1
                    else:
                        if target >= nums[M]:
                            L=M+1
                        else:
                            R=M-1
                else:
                    if target <= nums[R]:
                        if target >= nums[M]:
                            L=M+1
                        else:
                            R=M-1
                    else:
                        R=M-1
        return -1