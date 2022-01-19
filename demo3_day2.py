'''
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

输入：l1 = [0], l2 = [0]
输出：[0]
'''

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # 输入时list的时候
    def addTwoNumbersList(self, l1:list, l2:list):
        progression = 0 # 进位
        outList = []
        # 始终保持l1是较长的哪一个
        if len(l1) < len(l2):
            tempList = l1
            l1 = l2
            l2 = tempList

        for i in range(len(l2)):
            tempSum = l1[i] + l2[i] + progression
            outList.append(tempSum % 10)
            progression = int(tempSum / 10)

        if len(l1) > len(l2):
            for i in range(len(l2), len(l1)):
                tempSum = l1[i] + progression
                outList.append(tempSum % 10)
                progression = int(tempSum / 10)

        if progression:
            outList.append(1)

        return outList

    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        outLink = ListNode(0, None)
        progression = 0
        pl1 = l1
        pl2 = l2
        current = outLink
        while(pl1.next != None and pl2.next != None):
            tempSum = pl1.val + pl2.val + progression
            current.val = tempSum % 10
            progression = int(tempSum / 10)
            if pl1.next != None and pl2.next != None:
                current.next = ListNode(0, None)
                current = current.next

        while(pl1.next != None):
            current.next = ListNode(0, None)
            tempSum = pl1.val + progression
            current.next.val = tempSum % 10
            progression = int(tempSum / 10)
            current = current.next

        while (pl2.next != None):
            current.next = ListNode(0, None)
            tempSum = pl2.val + progression
            current.next.val = tempSum % 10
            progression = int(tempSum / 10)
            current = current.next

        if progression != 0:
            current.next = ListNode(1, None)

        return outLink






def main():
    solution = Solution()
    print(solution.addTwonumbers([9,9,9,9,9,9,9], [9,9,9,9]))


if __name__ == "__main__":
    main()





