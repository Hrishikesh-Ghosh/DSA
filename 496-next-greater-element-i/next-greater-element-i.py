class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        Stack = []
        next_greater = {}
        for x in nums2:
            while Stack and Stack[-1] < x:
                Popped = Stack.pop()
                next_greater[Popped] = x
            Stack.append(x)

        while Stack:
            Popped = Stack.pop()
            next_greater[Popped] = -1

        Result = []
        for i in nums1:
            Result.append(next_greater[i])

        return Result
