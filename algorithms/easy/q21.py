# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1ptr = l1
        list2ptr = l2
        prev = None
        curr = None
        root = None
        while list1ptr and list2ptr:
            if list1ptr.val<=list2ptr.val:
                curr = list1ptr
                list1ptr = list1ptr.next
            else:
                curr = list2ptr
                list2ptr = list2ptr.next
            if not root:
                root = curr
                prev = curr
            else:
                prev.next = curr
                prev = curr
                
        while list1ptr:
            curr = list1ptr
            list1ptr = list1ptr.next
            if not root:
                root = curr
                prev = curr
            else:
                prev.next = curr
                prev = curr
                
        while list2ptr:
            curr = list2ptr
            list2ptr = list2ptr.next
            if not root:
                root = curr
                prev = curr
            else:
                prev.next = curr
                prev = curr
                
        return root