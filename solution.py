# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    true_list = ListNode(0)
    current = true_list # creates a copy because it needs to iterate through and true_list would stay at the start of the list
    while list1 and list2:
        if list1.val > list2.val:
            current.next = list2 # this is .next and not .val because .next is a List while val is just a value.
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next
        current = current.next
    current.next = list1 or list2
    return true_list.next


# recursive solution
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def mergeTwoLists2( list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None: return list2
    if list2 == None: return list1
    if list1.val < list2.val:
        list1.next = mergeTwoLists2(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoLists2(list1, list2.next)
        return list2