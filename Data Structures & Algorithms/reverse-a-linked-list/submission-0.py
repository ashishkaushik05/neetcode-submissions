class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        a = None
        b = head
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        return a