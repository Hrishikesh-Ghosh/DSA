# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        Dummy = ListNode()
        DummyNodePointer = Dummy
        Dummy.next = head
        prevNode, currNode = Dummy, head
        while currNode and currNode.next:
            NodeAfterCurrNode = currNode.next
            prevNode.next = currNode.next
            currNode.next = NodeAfterCurrNode.next 
            NodeAfterCurrNode.next = currNode
        
            prevNode = currNode
            currNode = currNode.next
        return DummyNodePointer.next