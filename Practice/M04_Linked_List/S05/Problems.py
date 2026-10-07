# 876. Middle of the Linked List
''' 
# Solution1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid_ind = count // 2
        temp = head
        for i in range(mid_ind):
            temp = temp.next
        return temp
        '''
'''
# Solution2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
        '''
'''
# 141. Linked List Cycle
# Solution1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        temp = head
        while temp:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next
        return False
        
# Solution2
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    '''
'''
# 19. Remove Nth Node From End of List
# Solution1
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        dummy = ListNode()
        dummy.next = head
        temp = dummy
        for i in range(count - n):
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next
'''
