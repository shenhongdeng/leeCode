'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
'''

class Solution:
    def isValid(self, s: str):
        symbolQueue = []
        left = ["(", "[", "{"]
        right = [")", "]", "}"]
        right2left = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for char in s:
            if char in left:
                symbolQueue.append(char)
            if char in right:
                if len(symbolQueue) > 0: # 为空的时候不能pop
                    pop = symbolQueue.pop(-1)
                else:
                    return False
                if pop != right2left[char]:
                    return False

        if len(symbolQueue) > 0:
            return False
        return True











