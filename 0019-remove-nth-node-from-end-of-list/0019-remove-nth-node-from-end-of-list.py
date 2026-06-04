# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # In one pass find the total length of ll
    # In second pass traverse till curr_count < n and maintain prev_node
    # once we get n join prev_node to node.next
    # return fake_head.next
    # we will need one fake head for a condition where n is size where head will get deleted

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if not head:
            return None

        node = head
        count = 0

        while node:
            node = node.next
            count += 1
        
        ll_length = count
        num_deleted_node = ll_length - n

        count = 0
        node = head
        fake_head = ListNode()
        prev_node = fake_head

        while count < num_deleted_node:
            prev_node.next = node
            prev_node = node
            node = node.next
            count += 1

        prev_node.next = node.next
        node.next = None


        return fake_head.next
