'''
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
'''


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
    def removeNthFromEnd(self, head: ListNode, n: int):
        self.head = head
        length = self.lengthLink()
        self.remove(length - n + 1)
        return self.head



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
            node = None
        else:
            while (temp < pos - 1):
                node = node.next
                temp += 1
            node.next = node.next.next




link = sigleLink()
link.headInsert(3)
# link.headInsert(2)
# link.headInsert(1)
link.remove(1)
link.traersingLink()
print(link.lengthLink())


