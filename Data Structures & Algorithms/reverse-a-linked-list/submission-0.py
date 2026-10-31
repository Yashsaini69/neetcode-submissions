# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev = None
        curr = head

        while curr is not None:
            front = curr.next  # 1. Store next node so it isn't lost
            curr.next = prev  # 2. Reverse current node's pointer
            prev = curr  # 3. Move prev one step forward
            curr = front  # 4. Move curr one step forward

        return prev  # prev is pointing to the new head
