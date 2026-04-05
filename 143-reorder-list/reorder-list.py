# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Part 0: Taking care of cases where input is wrong
        if not head or not head.next:
            return
        #Part 1: Use fast and slow pointers to divide the linked list in two halves
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        Second = slow.next
        slow.next = None  
        #Part 2: Reverse the second link list from part 1
        prev = None
        curr = Second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr  
            curr = nxt
        Second = prev
        #Part 3: Merge the elements of the two linked lists consequtively
        First = head
        while Second:
            tmp1 = First.next
            tmp2 = Second.next
            First.next = Second
            Second.next = tmp1
            First = tmp1
            Second = tmp2
