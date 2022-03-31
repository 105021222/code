# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head=ListNode(0)
        tmp=head
        while(list1!=None and list2!=None):
            if list1.val<list2.val:
                tmp.next=list1
                list1=list1.next
            else:
                tmp.next=list2
                list2=list2.next
            tmp=tmp.next
        if list1!=None:
            tmp.next=list1
        else:
            tmp.next=list2
        return head.next
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """