# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class sigleLink:
    def __init__(self, node = None):
        self.head = node

    def headInsert(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def traersingLink(self):
        node = self.head
        while node is not None:
            print(node.val, end=' ')
            node = node.next

    def lengthLink(self):
        length = 0
        node = self.head
        while node is not None:
            node = node.next
            length += 1
        return length

    def remove(self, pos):
        temp = 1
        node = self.head
        if pos == 1:
            self.head = node.next
        else:
            while(temp < pos - 1):
                node = node.next
                temp += 1
            node.next = node.next.next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        plist1 = list1
        plist2 = list2
        newHead = None
        newTail = None
        if plist1 is None and plist2 is None:
            return newHead
        elif plist1 is None:
            return plist2
        elif plist2 is None:
            return plist1
        elif plist1.val < plist2.val:
            newHead = plist1
            newTail = plist1
            plist1 = plist1.next
        elif  plist1.val >= plist2.val:
            newHead = plist2
            newTail = plist2
            plist2 = plist2.next
        else:
            print("Error")
        print('here', plist1, plist2)

        while(plist1 is not None and plist2 is not None):
            node = ListNode()
            if plist1.val < plist2.val:
                node.val = plist1.val
                plist1 = plist1.next
            else:
                node.val = plist2.val
                plist2 = plist2.next
            newTail.next = node
            newTail = newTail.next

        # print(plist1)
        # print(plist2)
        if plist1 != None:
            newTail.next = plist1

        if plist2 != None:
            newTail.next = plist2
        return newHead


L1 = sigleLink()
# L1.headInsert(4)
L1.headInsert(2)
# L1.headInsert(1)
L2 = sigleLink()
# L2.headInsert(4)
# L2.headInsert(3)
L2.headInsert(1)
# L1.traersingLink()
print('')
# L2.traersingLink()
S = Solution()
L3 = sigleLink(S.mergeTwoLists(L1.head, L2.head))
print('')
L3.traersingLink()