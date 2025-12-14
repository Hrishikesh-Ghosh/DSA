# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        Stack = []
        current = head
        while current:
            Stack.append(current.val)
            current = current.next
        current = Stack.pop()
        maximum = current
        resultList = ListNode()
        resultList.val = maximum
        while Stack:
            current = Stack.pop()
            if current < maximum:
                continue
            else:
                newNode = ListNode()
                newNode.val = current
                newNode.next = resultList
                resultList = newNode
                maximum = current
        return resultList