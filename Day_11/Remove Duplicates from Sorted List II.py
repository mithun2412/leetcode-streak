class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        while curr:
            # check if current value is duplicated
            if curr.next and curr.val == curr.next.val:
                dup = curr.val
                # skip all nodes with this duplicate value
                while curr and curr.val == dup:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next

        return dummy.next

