# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        lst = []
        if temp != None:
            while temp != None:
                lst.append(temp)
                temp = temp.next
        for i in range(0, len(lst)):
            if i == 0:
                lst[i].next = None
            else:
                lst[i].next = lst[i-1]
            head = lst[i]
        return head