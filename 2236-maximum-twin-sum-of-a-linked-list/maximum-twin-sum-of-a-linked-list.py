# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        array = []
        while head:
            array.append(head.val)
            head = head.next
        lpointer = 0
        rpointer = len(array) - 1
        SumOfPointers = 0
        MaxSumOfPointersEver = 0
        for i in range(lpointer, rpointer):
            SumOfPointers = array[lpointer] + array[rpointer]
            lpointer += 1
            rpointer -= 1
            MaxSumOfPointersEver = max(MaxSumOfPointersEver, SumOfPointers)
        return MaxSumOfPointersEver