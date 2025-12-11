# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        values = []
        while head:
            values.append(head.val)
            head = head.next
        
        answer = [0]*len(values)
        stack = []

        for i, value in enumerate(values):
            while stack and value > values[stack[-1]]:
                answer[stack[-1]] = value
                stack.pop()
            stack.append(i)

        return answer