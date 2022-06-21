# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def to_num(l: Optional[ListNode]):
        ret = ""
        current = l
        while current != None:
            ret = str(current.val) + ret
            current = current.next
            
        return int(ret)
        
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = Solution.to_num(l1)
        n2 = Solution.to_num(l2)
        
        s = str(n1 + n2)[::-1]
        
        ret = None
        
        for char in s:
            if ret == None:
                ret = ListNode()
                current = ret
            else:
                current.next = ListNode()
                current = current.next
            current.val = int(char)
            
        return ret
        