'''
一个动态规划的问题，最长公共子串的问题

题目：
给你一个字符串 s，找到 s 中最长的回文子串

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

输入：s = "cbbd"
输出："bb"
'''

'''
思路暴力解法，最后部分解会超出时间限制
'''

class Solution():
    # 暴力的解法，遍历所有的起点和终点，然后判断每一个子串是不是回文串，并且记录最长的
    def longestPalindrome(self, s):
        maxLength = s[0]
        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if self.judgePalindrome(s[i: j+1]):
                    if (j - i) + 1 > len(maxLength):
                        maxLength = s[i:j + 1]
        return maxLength

    def judgePalindrome(self, s: str):
        # print('#', s)
        while(len(s) > 0):
            # print(s)
            if s[0] == s[-1]:
                s = s[1:-1]
            else:
                return False
        return True

def main():
    S = Solution()
    string = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    print(S.longestPalindrome(string))


if __name__ == "__main__":
    main()